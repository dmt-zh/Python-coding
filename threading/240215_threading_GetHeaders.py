# Создайте специализированный поток (через переопределения класса) получения заголовков интернет ресурсов со следующими свойствами:
# 1. Имя класса - GetHeaders;
# 2. Единственный задаваемый параметр - url: string. Ссылка на ресурс.
# 3. Параметр с результатом - url_headers в виде словаря где единственный ключ - url ссылка на ресурс. 
# Значение - словарь заголовков. Значение параметра по умолчанию - None.


import threading


class GetHeaders(threading.Thread):
    def __init__(self, url):
        self.url = url
        self.url_headers = {}
        super().__init__()

    def run(self):
        response = get_request_header(self.url)
        self.url_headers[self.url] = response