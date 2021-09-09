# Практика: методы
# Создайте метод greet для класса Person, который печатает сообщение "Hello, I am {name}!"
# Формат ввода: Имя человека.
# Формат вывода: Вывод метода приветствуем.
# Sample Input:
# David
# Sample Output:
# Hello, I am David!


class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f'Hello, I am {self.name.capitalize()}!')

person = Person(input().strip())
person.greet()