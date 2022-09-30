# В программе вводятся два значения в одну строчку через пробел. Значениями могут быть числа, слова, булевы величины
# (True/False). Необходимо прочитать эти значения из входного потока. Если оба значения являются числами,
# то вычислить их сумму, иначе соединить их в одну строку с помощью оператора + (конкатенации строк).
# Результат вывести на экран (в блоке finally).




class InputHandler:
    def __call__(self, *args, **kwargs):
        vars = input().strip().split()
        try:
            try:
                res = sum(map(int, vars))
            except ValueError:
                res = sum(map(float, vars))
        except:
            res = ''.join(map(str, vars))
        finally:
            print(res)


input_sum = InputHandler()
input_sum()
