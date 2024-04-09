# С использованием пула потоков запросите у yahoo.finance данные по ценам.
# Тикеры в файле - источнике укажите на свой вкус, например: AAPL, MSFT, AMZN, NVDA, TSLA, GOOGL, META, BRK-B, UNH, JPM.

# В качестве параметров запроса укажите недельный таймфрейм, интервал времени запроса - с начала 2020 года по настоящий день.

# Структура решения должна быть следующей:
# - пул потоков выполняет целевую задачу: функцию получения данных по запросу.
# - по мере получения ответа, данные попадают в потокобезопасную очередь данных.
# - отдельным потоком из очереди выполняется сохранение данных в .csv файл.
# - главный поток является управляющим, он только запускает потоки.

# Как и что именно хранить в csv файле, как его называть, как выполнять преобразование данных из ответа сервиса в данные
# для заполнения csv файла, обоработка ошибок - все это остается на ваше усмотрение. Не забывайте только, что данные csv
# файла нам нужны для будущего постороения графиков скорректированных цен.

# Необходимо нормализовать значения цен в ранее полученных файлах csv и создать общую наглядную картинку поведения ценных бумаг.

# Cделайте это задание с использованием нескольких потоков, придерживаясь следующего плана:
# - каждый поток считывает файл из каталога и преобразует его, добавляя третий столбец - нормализованная цена. 
#   Нормализованная цена - это значение в условных ед. с базой в 100 ед. Таким образом мы приведем различные цены к общему
#   масштабу (базовой единице) для обеспечения сопоставимости и удобства анализа
# - количество рабочих потоков необходимо ограничить. Предусмотрите возможность ограничения одновременно выполнящихся рабочих потоков
#   используя примитивы синхронизации.
# - оформите свое решение без применения пула потоков.
# - и, наконец, в главном потоке создайте общий график всех котировок с оформлением на свое усмотрение. 

# Формат, оформление, цвета, легенда, использование библиотеки - на ваш вкус.


import concurrent.futures
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import queue
import seaborn as sns
import requests
import threading

from datetime import date, datetime, timedelta, timezone
from dateutil.parser import parse
from time import sleep
from typing import Sequence, TypeAlias, Union

sns.set(style='whitegrid', font_scale=0.75)
TickerData: TypeAlias = Union[Sequence[str], Sequence[float], Sequence[datetime]]

def get_history_data(ticker: str, start_date: str, end_date: str, interval: str = "1wk") -> TickerData:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    params = {
        "period1": int(parse(start_date).replace(tzinfo=timezone.utc).timestamp()),
        "period2": int(parse(end_date).replace(tzinfo=timezone.utc).timestamp()),
        "interval": interval,
        "includeAdjustedClose": "true"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Connection': 'keep-alive'
    }
    try:
        response = requests.get(url, headers=headers, params=params).json()
        result = [
            [response['chart']['result'][0]['meta']['symbol']] * len(response['chart']['result'][0]['timestamp']),
            response['chart']['result'][0]['indicators']['adjclose'][0]['adjclose'],
            [datetime.fromtimestamp(stamp).date() for stamp in response['chart']['result'][0]['timestamp']]
        ]
    except Exception:
        print(f'Failed to get data for {ticker}')
        raise ValueError(f'{ticker}')
    return result


def csv_file_writer() -> None:
    os.makedirs('tickers_data', exist_ok=True)
    while True:
        data = tikers_data_queue.get()
        file_path = os.path.join('tickers_data', f'{data[0][0]}.csv')
        with open(file_path, 'w', encoding='utf-8', newline='') as fin:
            writer = csv.writer(fin, delimiter=';')
            writer.writerows(zip(*data))
        tikers_data_queue.task_done()


def results_handler(future: concurrent.futures.Future) -> None:
    exception = future.exception()
    if exception is not None:
        return
    try:
        data = future.result()
        tikers_data_queue.put(data)
    except Exception as err:
        print(f'Unknown error while handling data {err}')


class TickerNormalizer:
    def __init__(self, n_threads: int, ticker_seq: Sequence[str]) -> None:
        self.ticker_seq = ticker_seq
        self._semaphore = threading.Semaphore(n_threads)

    @staticmethod
    def _normilize(ticker_file: str) -> None:
        ticker_file_path = os.path.join('tickers_data', ticker_file)
        df = pd.read_csv(ticker_file_path, names=['company', 'price', 'date'], sep=';')
        df['normed_price'] = df.price * 100/df.price[0]
        df.to_csv(ticker_file_path, sep=';', index=False)

    def _process(self) -> None:
        for tiker in range(len(self.ticker_seq)):
            threading.Thread(target=self._task_runner, args=(f'{self.ticker_seq[tiker]}.csv', )).start()

    def _task_runner(self, ticker_file: str) -> None:
        with self._semaphore:
            self._normilize(ticker_file)

    def __call__(self) -> None:
        self._process()
        sleep(0.1)


def plot_tiker_data(ticker_seq: Sequence[str]) -> None:
    fin_df = pd.DataFrame()

    for ticker in ticker_seq:                                                                                                                 
        ticker_file_path = os.path.join('tickers_data', f'{ticker}.csv')                                                                     
        new_df = pd.read_csv(ticker_file_path, sep=';')              
        fin_df = pd.concat([fin_df, new_df], ignore_index=True)

    fin_df.to_csv(os.path.join('tickers_data', 'final_data.csv'), sep=';', index=False)
    ax = sns.lineplot(x='date', y='normed_price', hue='company', data=fin_df)
    ax.set(ylabel='Изменение цены, %', xlabel='Дата')
    ax.set_xticks([str(x.astype('datetime64[D]')) for x in np.arange(date(2020, 1, 1), date(2024, 4, 1), timedelta(weeks=22))])
    sns.despine()
    plt.legend(frameon=False, bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0)
    plt.show()
    

tickers_to_load = ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'TSLA', 'GOOGL', 'META', 'BRK-B', 'UNH', 'JPM']
tikers_data_queue = queue.Queue()

thr = threading.Thread(target=csv_file_writer, daemon=True)
thr.start()

with concurrent.futures.ThreadPoolExecutor() as executor:
    for ticker in tickers_to_load:
        future = executor.submit(get_history_data, ticker, '01/01/20', '01/04/24')
        future.add_done_callback(results_handler)

tikers_data_queue.join()

tiker_data_normize = TickerNormalizer(n_threads=2, ticker_seq=tickers_to_load)
tiker_data_normize()
plot_tiker_data(tickers_to_load)