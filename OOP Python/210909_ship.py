# Практика: методы.
# Переопределите метод sail нашего класса Ship, чтобы он взял пункт назначения
# и затем сказал бы, куда движется корабль. Вызовите этот метод для объекта black_pearl.

# Формат ввода: Название страны или города, куда идет корабль.
# Формат вывода: сообщение, структурированное как "The {name of the ship} has sailed for {country/city}!"

# Sample Input:
# Argentina

# Sample Output:
# The Black Pearl has sailed for Argentina!

class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def sail(self, country):
        self.country = country
        print(f'The {self.name} has sailed for {self.country}!')


black_pearl = Ship("Black Pearl", 800)
black_pearl.sail(input())