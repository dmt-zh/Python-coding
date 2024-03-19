# Есть список интернет-ресурсов. Необходимо получить заголовки всех этих страниц и сохранить результаты в словаре headers_stor,
# где ключ - ссылка на ресурс, а значение - возвращаемые функцией заголовки.

# Допишите программу с учетом того, что список ссылок и функция получения заголовков уже определена в тестирующей системе как:

# import requests

# sources = ["https://ya.ru",
#            "https://www.bing.com",
#            "https://www.google.ru",
#            "https://www.yahoo.com",
#            "https://mail.ru"]

# def get_request_header(url: str):
#     return requests.get(url).headers

# headers_stor = {}  # Храним здесь заголовки

# Вам необходимо только организовать создание и работу пула потоков. Тестирующая система проверяет время решения и содержимое хранилища заголовков.

# Напишите решение с использованием метода map().



import concurrent.futures

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    headers = executor.map(get_request_header, sources)

headers_stor = dict(zip(sources, headers))