# Перед Вами стоит задача -  скачать файлы и обработать их наиболее эффективным способом, используя полученные навыки.
# В качестве файлов будем скачивать картинки с хранилища NASA. В качестве обработки будем создавать миниатюры
# (их уменьшенные дубликаты, thumbnail).


from multiprocessing import Process, Queue, get_logger
from PIL import Image
from time import perf_counter
from typing import Final, Sequence

import concurrent.futures
import logging
import os
import requests


class ImageHandler:
    """ImageHandler.

    Downloads images by urls and resizes them.
    """

    def __init__(
        self,
        max_height: int,
        max_width: int,
        img_urls: Sequence[str],
        workdir: str,
        n_jobs: int = 2,
    ) -> None:
        self._max_hight: Final = max_height
        self._max_width: Final = max_width
        self._img_urls: Final = img_urls
        self._n_jobs: Final = n_jobs
        self._download_dir: Final = os.path.join(workdir, 'original')
        self._output_dir: Final = os.path.join(workdir, 'resized')
        self._images_to_process = Queue()
        self._logger = self._initialize_logger()

    ######################################################################################

    @staticmethod
    def _initialize_logger():
        logging.basicConfig(level=logging.INFO, format='{processName}, {threadName}, {asctime}, {message}', style='{')
        logger = get_logger()
        info_handler = logging.FileHandler('logging_info.txt', encoding='utf8')
        info_handler.setLevel(logging.INFO)
        errors_handler = logging.FileHandler('logging_errors.txt', encoding='utf8')
        errors_handler.setLevel(logging.ERROR)
        logger.addHandler(info_handler)
        logger.addHandler(errors_handler)
        return logger

    ######################################################################################

    def _download_img(self, url: str) -> str | None:
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            filename = url.split('/')[-1]

            download_path = os.path.join(self._download_dir, filename)
            with open(download_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=4096):
                    file.write(chunk)

            self._logger.info(f'Успешно загружено изображение: {url}')
            return os.path.abspath(download_path)
        except requests.exceptions.RequestException:
            self._logger.error(f'Ошибка при загрузке изображения по адресу: {url}')

    ######################################################################################

    def _process_img(self) -> None:
        while (image_file := self._images_to_process.get()) is not None:
            _, filename = os.path.split(image_file)
            resized_filename = f'resized_{filename}'
            resized_path = os.path.abspath(os.path.join(self._output_dir, resized_filename))
            try:
                image = Image.open(image_file)
                image.thumbnail((self._max_width, self._max_hight))
                image.save(resized_path)
                self._logger.info(f'Успешно обработано изображение: {filename}')
            except IOError:
                self._logger.error(f'Ошибка при обработке файла: {filename}')

        if image_file is None:
            self._images_to_process.put(None)

    ######################################################################################
                
    def _put_img_in_queue(self, future: concurrent.futures.Future) -> None:
        downloaded_img = future.result()
        if downloaded_img:
            self._images_to_process.put(downloaded_img)

    ######################################################################################

    def run(self) -> None:
        os.makedirs(self._download_dir, exist_ok=True)
        os.makedirs(self._output_dir, exist_ok=True)
        workers = [Process(target=self._process_img) for _ in range(self._n_jobs)]
        for worker in workers:
            worker.start()

        with concurrent.futures.ThreadPoolExecutor() as thread_executor:
            for url in self._img_urls:
                thread_executor.submit(self._download_img, url).add_done_callback(self._put_img_in_queue)

        self._images_to_process.put(None)

        for worker in workers:
            worker.join()


urls = [
    'https://apod.nasa.gov/apod/image/2310/IC63_GruntzBax.jpg',
    'https://apod.nasa.gov/apod/image/2310/2P_Encke_2023_08_24JuneLake_California_USA_DEBartlett.jpg',
    'https://apod.nasa.gov/apod/image/2310/20231023_orionids_in_taurus_1440b.jpg',
    'https://apod.nasa.gov/apod/image/2310/Arp87_HubblePathak_2512.jpg',
    'https://apod.nasa.gov/apod/image/2310/C2023H2LemmonGalaxies.jpg',
    'https://apod.nasa.gov/apod/image/2310/WesternVeil_Wu_2974.jpg',
    'https://apod.nasa.gov/apod/image/2310/M33_Triangulum.jpg',
    'https://apod.nasa.gov/apod/image/2310/MuCephei_apod.jpg',
    'https://apod.nasa.gov/apod/image/2310/Hourglass_HubblePathak_1080.jpg',
    'https://apod.nasa.gov/apod/image/2310/HiResSprites_Escurat_3000.jpg',
    'https://apod.nasa.gov/apod/image/2309/M8-Mos-SL10-DCPrgb-st-154-cC-cr.jpg',
    'https://apod.nasa.gov/apod/image/2309/BlueHorse_Grelin_93.jpg',
    'https://apod.nasa.gov/apod/image/2309/Arp142_HubbleChakrabarti_2627.jpg',
    'https://apod.nasa.gov/apod/image/2309/HH211_webb_3846.jpg',
    'https://apod.nasa.gov/apod/image/2309/LRGBHa23_n7331r.jpg',
    'https://apod.nasa.gov/apod/image/2309/PolarRing_Askap_960.jpg',
    'https://apod.nasa.gov/apod/image/2309/STSCI-HST-abell370_1797x2000.jpg'
]


if __name__ == '__main__':
    start_time = perf_counter()
    image_handler = ImageHandler(
        max_height=400,
        max_width=600,
        img_urls=urls,
        workdir='./nasa_foto'
    )
    image_handler.run()
    print(f'ALL DONE, {perf_counter() - start_time}')