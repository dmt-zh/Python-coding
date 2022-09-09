# Oбъявите в программе класс с именем: Singleton который бы позволял создавать только один экземпляр
# (все последующие экземпляры должны ссылаться на первый).

# Затем, объявите еще один класс с именем: Game который бы наследовался от класса Singleton. Объекты класса
# Game должны создаваться командой: game = Game(name)
# где name - название игры (строка). В каждом объекте класса Game должен создаваться атрибут name с соответствующим
# содержимым. Убедитесь, что атрибут name принимает значение первого созданного объекта (если это не так,
# то поправьте инициализатор дочернего класса, чтобы это условие выполнялось).




class Singleton:
    __instance = None
    __instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if not cls.__instance_base:
                cls.__instance_base = super().__new__(cls)
            return cls.__instance_base

        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


class Game(Singleton):
    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name
