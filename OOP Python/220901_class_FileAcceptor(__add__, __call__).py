# Перед вами стоит задача выделения файлов с определенными расширениями из списка файлов, например:
# filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg",
# "eq_1.png", "eq_2.xls"]

# Для этого необходимо объявить класс FileAcceptor, объекты которого создаются командой:
# acceptor = FileAcceptor(ext1, ..., extN)
# где ext1, ..., extN - строки с допустимыми расширениями файлов, например: 'jpg', 'bmp', 'jpeg'.

# После этого предполагается использовать объект acceptor в стандартной функции filter языка Python следующим образом:
# filenames = list(filter(acceptor, filenames))

# То есть, объект acceptor должен вызываться как функция:
# acceptor(filename) и возвращать True, если файл с именем filename содержит расширения, указанные при
# создании acceptor, и False - в противном случае. Кроме того, с объектами класса FileAcceptor должен 
# выполняться оператор: acceptor12 = acceptor1 + acceptor2

# Здесь формируется новый объект acceptor12 с уникальными расширениями первого и второго объектов. 
# Например:

# acceptor1 = FileAcceptor("jpg", "jpeg", "png")
# acceptor2 = FileAcceptor("png", "bmp")
# acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")



class FileAcceptor:
    def __init__(self, *args):
        self.__exts = list(set(args))

    def get_extensions(self):
        return self.__exts

    def __add__(self, other):
        if isinstance(other, FileAcceptor):
            lst_self = self.__exts[:]
            lst_other = other.get_extensions()[:]
            return FileAcceptor(*set(lst_self + lst_other))

    def __call__(self, file_name, *args, **kwds):
        ext = file_name.rsplit('.', 1)[-1]
        return ext in self.__exts