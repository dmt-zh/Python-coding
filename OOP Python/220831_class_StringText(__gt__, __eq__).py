# Имеется стихотворение, представленное следующим списком строк:
# stich = ["Я к вам пишу – чего же боле?",
#         "Что я могу еще сказать?",
#         "Теперь, я знаю, в вашей воле",
#         "Меня презреньем наказать.",
#         "Но вы, к моей несчастной доле",
#         "Хоть каплю жалости храня,",
#         "Вы не оставите меня."]

# Необходимо в каждой строчке этого стиха убрать символы "–?!,.;" в начале и в конце каждого слова 
# и разбить строку по словам (слова разделяются одним или несколькими пробелами). На основе 
# полученного списка слов, создать объект класса StringText командой:

# st = StringText(lst_words)
# где lst_words - список из слов одной строчки стихотворения. 

# С объектами класса StringText должны быть реализованы операторы сравнения:
# st1 > st2   # True, если число слов в st1 больше, чем в st2
# st1 >= st2  # True, если число слов в st1 больше или равно st2
# st1 < st2   # True, если число слов в st1 меньше, чем в st2
# st1 <= st2  # True, если число слов в st1 меньше или равно st2
# Все объекты класса StringText (для каждой строчки стихотворения) сохранить в списке lst_text. 
# Затем, сформировать новый список lst_text_sorted из отсортированных объектов класса StringText по 
# убыванию числа слов. Для сортировки использовать стандартную функцию sorted() языка Python. 
# После этого преобразовать данный список (lst_text_sorted) в список из строк (объекты заменяются 
# на соответствующие строки, между словами ставится пробел).




import re

class StringText:
    def __init__(self, words):
        self.words = words

    @classmethod
    def __valid_types(cls, obj):
        return isinstance(obj, StringText)

    def __len__(self):
        return len(self.words)

    def __eq__(self, other):
        if self.__valid_types(other):
            return len(self) == len(other)

    def __gt__(self, other):
        if self.__valid_types(other):
            return len(self) > len(other)

    def __ge__(self, other):
        if self.__valid_types(other):
            return len(self) >= len(other)

    def __str__(self):
        return ' '.join(self.words)



stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

lst_words = [re.sub("[^А-Яа-я\s]", '', i).split() for i in stich]
lst_text = [StringText(lst) for lst in lst_words]
lst_text_sorted = list(map(str, sorted(lst_text, reverse=True)))