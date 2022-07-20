# Представьте, что вы получили задание от заказчика. Вас просят реализовать простую имитацию локальной сети,
# состоящую из набора серверов, соединенных между собой через роутер.
# Каждый сервер может отправлять пакет любому другому серверу сети. Для этого у каждого есть свой уникальный IP-адрес.
# Для простоты - это просто целое (натуральное) число от 1 и до N, где N - общее число серверов. Алгоритм следующий.
# Предположим, сервер с IP = 2 собирается отправить пакет информации серверу с IP = 3. Для этого, он сначала отправляет
# пакет роутеру, а уже тот, смотрит на IP-адрес и пересылает пакет нужному узлу (серверу).

# Для реализации этой схемы программе предлагается объявить три класса:
# Server - для описания работы серверов в сети;
# Router - для описания работы роутеров в сети (в данной задаче полагается один роутер);
# Data - для описания пакета информации.

# Серверы будут создаваться командой:
# sv = Server()

# При этом, уникальный IP-адрес каждого сервера должен формироваться автоматически при создании нового экземпляра класса Server.
# Далее, роутер должен создаваться аналогичной командой:
# router = Router()

# А, пакеты данных, командой:
# data = Data(строка с данными, IP-адрес назначения)

# Для формирования и функционирования локальной сети, в классе Router должны быть реализованы следующие методы:
# link(server) - для присоединения сервера server (объекта класса Server) к роутеру (для простоты, каждый сервер
# соединен только с одним роутером);
# unlink(server) - для отсоединения сервера server (объекта класса Server) от роутера;
# send_data() - для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам (после отправки буфер должен очищаться).

# И одно обязательное локальное свойство (могут быть и другие свойства):
# buffer - список для хранения принятых от серверов пакетов (объектов класса Data).

# Класс Server должен содержать свой набор методов:
# send_data(data) - для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
# (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
# get_data() - возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список) и очищает
# входной буфер;
# get_ip() - возвращает свой IP-адрес.

# Соответственно в объектах класса Server должны быть локальные свойства:
# buffer - список принятых пакетов (объекты класса Data, изначально пустой);
# ip - IP-адрес текущего сервера.

# Наконец, объекты класса Data должны содержать два следующих локальных свойства:
# data - передаваемые данные (строка);
# ip - IP-адрес назначения.

# Ваша задача реализовать классы Router, Server и Data в соответствии с приведенным техническим заданием (ТЗ).



class Server:
    __instance = None
    __ip = 0
    def __new__(cls, *args, **kwargs):
        if cls.__ip < 10**5:
            cls.__instance = super().__new__(cls)
            cls.__ip += 1
        return cls.__instance

    def __init__(self):
        self.buffer = []
        self.ip = self.__ip
        self.router = None

    def send_data(self, data):
        if self.router is not None:
            self.router.buffer.append(data)

    def get_data(self):
        buffered_data = self.buffer[:]
        self.buffer.clear()
        return buffered_data

    def get_ip(self):
        return self.ip

    def link_to_router(self, router):
        self.router = router


class Router:
    def __init__(self):
        self.linked_sevrers = dict()
        self.buffer = list()
        self.router_link = self

    def link(self, server):
        key = server.ip
        if key in self.linked_sevrers:
            pass
        else:
            self.linked_sevrers[key] = server
            server.router = self.router_link

    def unlink(self, server):
        key = server.ip
        if key in self.linked_sevrers:
            self.linked_sevrers.pop(key)
        pass

    def send_data(self):
        for data in self.buffer:
            server_id = data.ip
            server = self.linked_sevrers.get(server_id, False)
            if server:
                server.buffer.append(data)

        self.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip