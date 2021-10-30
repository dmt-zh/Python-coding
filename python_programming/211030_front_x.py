# Напишите функцию front_x(words), которая на вход принимает список строк и возвращает отсортированный по правилам:
# - слова, начинающиеся с символа "x", идут первыми
# - в лексикографическом порядке.
# Важно! Список может содержать пустые строки - "" - их нельзя выкидывать и при их обработке функция не должна "падать".
#
# Sample Input:
# ['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']

# Sample Output:
# ['x-files', 'xapple', 'xyz', '', 'apple', 'extra', 'mix']


def front_x(words):
    return sorted(words, key=lambda x: (not x.startswith('x'), x))