# Реализуйте функцию scrabble(), которая принимает два аргумента в следующем порядке:
# symbols — набор символов
# word — слово

# Функция должна возвращать True, если из набора символов symbols можно составить слово word, или False в противном случае.
# Примечание. При проверке учитывается количество символов, которые нужны для составления слова, и не учитывается их регистр.



from collections import Counter


def scrabble(letters, word):
    return Counter(letters.lower()) >= Counter(word.lower())