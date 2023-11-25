# Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:

# start — дата, тип date
# count — натуральное число, по умолчанию имеет значение None
# Если count имеет значение None, функция должна возвращать генератор, порождающий последовательность из максимально допустимого
#  количества дат (тип date), начиная с даты start.

# Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий последовательность
#  из count дат (тип date), начиная с даты start, а затем возбуждающий исключение StopIteration.


from datetime import date, timedelta

def dates(start_date, num=None):
    end_date = (date.max - start_date).days + 1 if num is None else num
    for delta in range(end_date):
        yield start_date + timedelta(days=delta)