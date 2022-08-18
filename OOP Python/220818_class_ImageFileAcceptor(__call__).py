# Для последовательной обработки файлов из некоторого списка, например:
# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg",
# "eq_1.png", "eq_2.png", "my.html", "data.shtml"]

# Необходимо объявить класс ImageFileAcceptor, который бы выделял только файлы с указанными расширениями.
# Для этого предполагается создавать объекты класса командой:
# acceptor = ImageFileAcceptor(extensions)
# где extensions - кортеж с допустимыми расширениями файлов, например: extensions = ('jpg', 'bmp', 'jpeg').

# А, затем, использовать объект acceptor в стандартной функции filter языка Python следующим образом:
# image_filenames = filter(acceptor, filenames)

# Пример использования класса (эти строчки в программе писать не нужно):
# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
# acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
# image_filenames = filter(acceptor, filenames)
# print(list(image_filenames)) ["boat.jpg", "ava.jpg", "forest.jpeg"]



class ImageFileAcceptor:
    def __init__(self, extensions):
        self.__args = extensions

    def __call__(self, file_name, *args, **kwargs):
        ext = None
        if type(file_name) == str:
            ext = file_name.split('.')[-1]
        else:
            raise TypeError('Проверяемое имя файла должно быть строкой.')
        return ext in self.__args