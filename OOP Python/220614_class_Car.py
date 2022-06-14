# Объявите пустой класс с именем Car. С помощью функции setattr() добавьте в этот класс атрибуты:
# model: "Тойота"
# color: "Розовый"
# number: "П111УУ77"
# Выведите на экран значение атрибута color, используя словарь __dict__ класса Car.


props = {'model': "Тойота", 'color': "Розовый", 'number': "П111УУ77"}

class Car:
    pass


for k, v in props.items():
    setattr(Car, k, v)

print(Car.__dict__.get('color'))