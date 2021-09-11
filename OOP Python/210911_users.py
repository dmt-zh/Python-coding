#  Практика: методы и атрибуты. Метод add_friends класса User был определен неправильно. 
# Этот метод должен увеличивать количество друзей у пользователя на значение n. Исправьте
#  ошибки в методе.


class User:
    def __init__(self, username):
        self.username = username
        self.friends = 0

    # fix this method
    def add_friends(self, n):
        self.friends += n
        print("{} now has {} friends.".format(self.username, self.friends))
