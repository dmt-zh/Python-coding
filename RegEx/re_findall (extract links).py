# Выведите все ссылки, которые находятся в тегах a:
# <a target="_blank" href="https://stepik.org/">Hyperlink</a>

# Должно вывести: https://stepik.org/

# Sample Input 1:
# <html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge">
# <meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Пролистай вниз</title>
# <link rel="stylesheet" href="./css/normalize.css"><link rel="stylesheet" href="./css/style.css">
# <link rel="icon" href="./img/icon.jpg"></head><body><header><h1 class="privet">Привет!<br>Пролистай страничку вниз.
# </h1><img src="./img/photo.jpg" alt="" class="logo_icon"></header><main><p class="paragraph">
# Чтобы продолжить - отправь боту любое фото.</p></main><footer><a class="link" href="./img/photo.jpg" download="">
# Фото</a><p class="link">id стикера - CAACAgIAAxkBAAIDxWITCaZnaUelQ0SNlHMTrjd2klAmAAIBAQACVp29CiK-nw64wuY0IwQ
# </p><a class="link" href="./img/tochno.txt" download="">Документ</a></footer></body></html>

# Sample Output 1:
# ./img/photo.jpg
# ./img/tochno.txt



import re

links = re.findall(r'(?<=<a).*?href=\"(.*?)\"', input())
print(*links, sep='\n')