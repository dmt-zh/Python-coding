# Необходимо написать универсальную основу для представления ненаправленных связных графов и поиска в
# них кратчайших маршрутов. Далее, этот алгоритм предполагается применять для прокладки маршрутов: на картах,
# в метро и так далее.

# Для универсального описания графов, вам требуется объявить в программе следующие классы:
# Vertex - для представления вершин графа (на карте это могут быть: здания, остановки, достопримечательности и т.п.);
# Link - для описания связи между двумя произвольными вершинами графа (на карте: маршруты, время в пути и т.п.);
# LinkedGraph - для представления связного графа в целом (карта целиком).


# Объекты класса Vertex должны создаваться командой: v = Vertex() и содержать локальный атрибут:
# _links - список связей с другими вершинами графа (список объектов класса Link).Также в этом классе должно быть
# объект-свойство (property): links - для получения ссылки на список _links.

# Объекты следующего класса Link должны создаваться командой:
# link = Link(v1, v2)
# где v1, v2 - объекты класса Vertex (вершины графа).

# Внутри каждого объекта класса Link должны формироваться следующие локальные атрибуты:
# _v1, _v2 - ссылки на объекты класса Vertex, которые соединяются данной связью;
# _dist - длина связи (по умолчанию 1); это может быть длина пути, время в пути и др.

# В классе Link должны быть объявлены следующие объекты-свойства:
# v1 - для получения ссылки на вершину v1;
# v2 - для получения ссылки на вершину v2;
# dist - для изменения и считывания значения атрибута _dist.

# Наконец, объекты третьего класса LinkedGraph должны создаваться командой:  map_graph = LinkedGraph()
# В каждом объекте класса LinkedGraph должны формироваться локальные атрибуты:
# _links - список из всех связей графа (из объектов класса Link);
# _vertex - список из всех вершин графа (из объектов класса Vertex).

# В самом классе LinkedGraph необходимо объявить (как минимум) следующие методы:
# def add_vertex(self, v): ... - для добавления новой вершины v в список _vertex (если она там отсутствует);
# def add_link(self, link): ... - для добавления новой связи link в список _links (если объект link с указанными
# вершинами в списке отсутствует);
# def find_path(self, start_v, stop_v): ... - для поиска кратчайшего маршрута из вершины start_v в вершину stop_v.

# Метод find_path() должен возвращать список из вершин кратчайшего маршрута и список из связей этого же маршрута
# в виде кортежа: ([вершины кратчайшего пути], [связи между вершинами])

# В методе add_link() при добавлении новой связи следует автоматически добавлять вершины этой связи в список _vertex,
# если они там отсутствуют. Проверку наличия связи в списке _links следует определять по вершинам этой связи.
# Например, если в списке имеется объект: _links = [Link(v1, v2)] то добавлять в него новые объекты Link(v2, v1)
# или Link(v1, v2) нельзя (обратите внимание у всех трех объектов будут разные id, т.е. по id определять вхождение
# в список нельзя).




class Vertex:
    def __init__(self):
        self._links = list()

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2):
        self._v1, self._v2 = v1, v2
        self._dist = 1
        self.__stations = (v1, v2)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    def __eq__(self, other):
        if isinstance(other, Link):
            return other._v1 in self.__stations and other._v2 in self.__stations
        else:
            return other[0] in self.__stations and other[1] in self.__stations


class LinkedGraph:
    def __init__(self):
        self._links = list()
        self._vertex = list()

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        self.add_vertex(link.v1)
        self.add_vertex(link.v2)
        if not any((map(lambda x: x == link, self._links))):
            self._links.append(link)

    def __get_all_stations(self, vs=False):
        if vs:
            return {k: v for k, v in enumerate(self._vertex)}
        else:
            return {v: k for k, v in enumerate(self._vertex)}

    def __get_vertex_grid(self):
        all_stations = self.__get_all_stations()
        indexes_and_weights = {(all_stations[st.v1], all_stations[st.v2]): st.dist for st in self._links}
        grid = [[float('inf') for _ in range(len(self._vertex))] for _ in range(len(self._vertex))]
        for indexes, weight in indexes_and_weights.items():
            row, col = indexes
            grid[row][col] = weight
            grid[col][row] = weight
        return grid

    @staticmethod
    def __get_graph_paths(matrix):
        size = len(matrix)
        paths = [list(range(size)) for _ in range(size)]

        for k in range(size):
            for i in range(size):
                for j in range(size):
                    d = matrix[i][k] + matrix[k][j]
                    if matrix[i][j] > d:
                        matrix[i][j] = d
                        paths[i][j] = k
        return paths

    def __get_path(self, P, u, v):
        path = [u]
        while u != v:
            u = P[u][v]
            path.append(u)
        return path[::-1]

    def __get_stations_links(self, path):
        stations = [tuple(path[i:i + 2]) for i in range(len(path) - 1)]
        route_links = [link for st in stations for link in self._links if st == link]
        return route_links

    def find_path(self, start_v, stop_v):
        mtx = self.__get_vertex_grid()
        graph_paths = self.__get_graph_paths(mtx)

        all_stations = self.__get_all_stations()
        keys = self.__get_all_stations(vs=True)

        start = all_stations.get(start_v)
        end = all_stations.get(stop_v)

        shortest_path = self.__get_path(graph_paths, end, start)
        stations_path = [keys.get(st) for st in shortest_path]
        stations_links = self.__get_stations_links(stations_path)
        return stations_path, stations_links


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist
        v1.links.append(v2)
        v2.links.append(v1)

    def __repr__(self):
        return f"'{self.v1}'=>'{self.v2}'={self.dist}"



map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7







