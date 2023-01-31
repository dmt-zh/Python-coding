# Вам дана следующая структура файла в формате JSON:

# [
# {
#     "id": 1,
#     "login": "gafgsd",
#     "password": "gsdffsd",
#     "email": "sh@ya.ru",
#     "date": "2022-12-12",
#     "status": 2,
#     "is_moderator": false
# },
# {
#     "id": 2,
#     "login": "antory",
#     "password": "passworD2",
#     "email": "sh@ya.ru",
#     "date": "2021-10-15",
#     "status": 1,
#     "is_moderator": true
# },
# ...
# ]

# Вам известно, что за поля должны к вам приходить, и какое должно быть в них содержимое:
# id – int, обязательное
# login – str, обязательное, минимальная длина 3 и максимальная 20 символов
# password – str, обязательное, минимальная длина 3 и максимальная 50 символов, имеется хотя бы одна цифра и буква в верхнем регистре
# email – str, опциональное, подходит под шаблон: {a}@{b}.{c}
# date – str, опциональное, дата в формате ISO – YYYY-mm-dd
# status – int, обязательное, один из статусов 1,5,7,9,14
# is_moderator – bool, опциональное

# Отвалидируйте файл file.json. В качестве результата для каждого пользователя в случае если все в порядке запишите OK,
# в ином случае строку Failed. Ответы записывайте через запятую.
# Failed,OK,...


from pydantic import BaseModel, constr, parse_obj_as, validator
import json


class UserValidator(BaseModel):
    id: int
    login: constr(min_length=3, max_length=20)
    password: constr(min_length=3, max_length=50, regex=".*[A-Z].*")
    email: constr(min_length=7, max_length=50, regex="^\w+@\w+\.\w{2,5}$") | None
    date: constr(regex="^[1-2]\d{3}-[0-3]\d-\d{1,2}$") | None
    status: int
    is_moderator: bool | None

    @validator("status")
    def valid_status(cls, value: str):
        assert value in [1, 5, 7, 9, 14]


res = []

with open("dataset.txt", encoding='utf8') as fin:
    raw_data = json.load(fin)

    for raw_user in raw_data:
        try:
            user_obj = parse_obj_as(UserValidator, raw_user)
            res.append('OK')
        except:
            res.append('Failed')

print(*res, sep=',')