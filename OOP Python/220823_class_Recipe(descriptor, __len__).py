# Объявите класс Recipe для представления рецептов. Отдельные ингредиенты рецепта должны определяться классом Ingredient.
# Объекты этих классов должны создаваться командами:

# ing = Ingredient(name, volume, measure)
# recipe = Recipe()
# recipe = Recipe(ing_1, ing_2,..., ing_N)
# где ing_1, ing_2,..., ing_N - объекты класса Ingredient.

# В каждом объекте класса Ingredient должны создаваться локальные атрибуты:
# name - название ингредиента (строка);
# volume - объем ингредиента в рецепте (вещественное число);
# measure - единица измерения объема ингредиента (строка), например, литр, чайная ложка, грамм, штук и т.д.;

# С объектами класса Ingredient должна работать функция:
# str(ing)  # название: объем, ед. изм.
# и возвращать строковое представление объекта в формате: "название: объем, ед. изм."

# Например:
# ing = Ingredient("Соль", 1, "столовая ложка")
# s = str(ing) # Соль: 1, столовая ложка

# Класс Recipe должен иметь следующие методы:
# add_ingredient(ing) - добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец);
# remove_ingredient(ing) - удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;
# get_ingredients() - получение кортежа из объектов класса Ingredient текущего рецепта.

# Также с объектами класса Recipe должна поддерживаться функция:
# len(recipe) - возвращает число ингредиентов в рецепте.




class BaseIngredient:
    def __set_name__(self, owner, name):
        self.__name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.__name)

    def __set__(self, instance, value):
        key = f'{self.__name}'.split('_')[-1]
        if not isinstance(value, (float, str)) and key not in ('name', 'volume', 'measure'):
            raise AttributeError('Incorrect data format, try strings and floats.')
        setattr(instance, self.__name, value)


class Ingredient:
    name = BaseIngredient()
    volume = BaseIngredient()
    measure = BaseIngredient()

    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:
    def __init__(self, *args):
        self.__book = list(args)

    def add_ingredient(self, ing):
        self.__book.append(ing)

    def remove_ingredient(self, ing):
        if ing in self.__book:
            self.__book.remove(ing)

    def get_ingredients(self):
        return tuple(self.__book)

    def __len__(self):
        return self.__book.__len__()