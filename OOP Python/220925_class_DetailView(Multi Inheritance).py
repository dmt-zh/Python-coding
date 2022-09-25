# Предположим, что в программе уже существует следующий набор классов:

# class RetriveMixin:
#     def get(self, request):
#         return "GET: " + request.get('url')

# class CreateMixin:
#     def post(self, request):
#         return "POST: " + request.get('url')

# class UpdateMixin:
#     def put(self, request):
#         return "PUT: " + request.get('url')

# Здесь в каждом классе выполняется имитация обработки запросов. За GET-запрос отвечает метод get() класса
# RetriveMixin, за POST-запрос - метод post() класса CreateMixin, за PUT-запрос - метод put() класса UpdateMixin.
#
# Далее, вам нужно объявить класс с именем GeneralView, в котором следует указать атрибут (на уровне класса):
# allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
# для перечня разрешенных запросов. А также объявить метод render_request со следующей сигнатурой:
# def render_request(self, request): ...

# Здесь request - это словарь (объект запроса), в котором обязательно должны быть два ключа:
# 'url' - адрес для обработки запроса;
# 'method' - метод запроса: 'GET', 'POST', 'PUT', 'DELETE' и т. д.
#
# В методе render_request() нужно сначала проверить, является ли указанный запрос в словаре request разрешенным
# (присутствует в списке allowed_methods). И если это не так, то генерировать исключение командой:
# raise TypeError(f"Метод {request.get('method')} не разрешен.")

# Иначе, вызвать метод по его имени:
# method_request = request.get('method').lower()  # имя метода, малыми буквами

# Для использования полученных классов, в программе объявляется следующий дочерний класс:
# class DetailView(RetriveMixin, GeneralView):
#     allowed_methods = ('GET', 'PUT', )

# Воспользоваться им можно, например, следующим образом (эти строчки в программе не писать):
# view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
# print(html)   # GET: https://stepik.org/course/116336/

# Если в запросе указать другой метод:
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
# то естественным образом возникнет исключение (реализовывать в программе не нужно, это уже
# встроено в сам язык Python):
# AttributeError: 'DetailView' object has no attribute 'put'

# так как дочерний класс DetailView не имеет метода put. Поправить это можно, если указать соответствующий
# базовый класс:

# class DetailView(RetriveMixin, UpdateMixin, GeneralView):
#     allowed_methods = ('GET', 'PUT', )

# Теперь, при выполнении команд:
# view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
# print(html) # будет выведено: PUT: https://stepik.org/course/116336/

# В программе требуется объявить только класс GeneralView.



class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        method = request.get('method').upper()
        if method not in self.allowed_methods:
            raise TypeError(f"Метод {method} не разрешен.")

        method_request = self.__getattribute__(method.lower())
        if method_request:
            return method_request(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )




view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
print(html)
