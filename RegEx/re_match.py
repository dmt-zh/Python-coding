# Вы богатый и состоятельный человек. На вашу почту отправляются тысячи писем в месяц с предложением сотрудничества.
# Напишите программу, которая будет определять некультурных людей, не здоровающихся с вами в письмах. Если строка
# начинается с "Здравствуйте" или "Hello", то выводите на экран "Ну привет!", иначе выводите "Фу, как некультурно!".
# На вход программе подаётся строка. Нужно определить, начинается ли она с нужных слов или нет, и вывести соответствующий
# ответ в консоль.



import re

class EmailFilter:
    def __init__(self, re_pattern):
        self._pattern = re_pattern

    def __call__(self, email, *args, **kwargs):
        has_greeting = re.match(self._pattern, email)
        if has_greeting:
            print('Ну привет!')
        else:
            print('Фу, как некультурно!')


check_email = EmailFilter(r'Здравствуйте|Hello')
check_email(input().strip())
