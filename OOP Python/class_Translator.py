# Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:
# add(self, eng, rus) - для добавления новой связки английского и русского слова (если английское слово уже существует,
# то новое русское слово добавляется как синоним для перевода, например, go - идти, ходить, ехать);
# remove(self, eng) - для удаления связки по указанному английскому слову;
# translate(self, eng) - для перевода с английского на русский (метод должен возвращать список из русских слов, соответствующих
# переводу английского слова, даже если в списке всего одно слово).

# Создайте экземпляр tr класса Translator и вызовите метод add для следующих связок:
# tree - дерево
# car - машина
# car - автомобиль
# leaf - лист
# river - река
# go - идти
# go - ехать
# go - ходить
# milk - молоко

# Затем методом remove() удалите связку для английского слова car. С помощью метода translate() переведите слово go.
# Результат выведите на экран в виде строки из всех русских слов, связанных со словом go:
# Вывод в формате: идти ехать ходить

s = """
tree - дерево
car - машина
car - автомобиль
leaf - лист
river - река
go - идти
go - ехать
go - ходить
milk - молоко
"""

pairs = s.strip().replace(' - ', ' ').split('\n')

class Translator:
    def add(self, eng, rus):
        if 'words' not in self.__dict__:
            self.words = {}

        self.words.setdefault(eng, [])
        self.words[eng].append(rus)

    def remove(self, eng):
        self.words.pop(eng, False)

    def translate(self, eng):
        return self.words[eng]


tr = Translator()

for pair in pairs:
    k, v = pair.split()
    tr.add(k, v)

tr.remove('car')
print(' '.join(tr.translate('go')))