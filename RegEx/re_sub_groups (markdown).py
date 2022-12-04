# Markdown в HTML
# Замените **Жирный текст** на <strong>Жирный текст</strong>, и *Курсив* на <em>Курсив</em>.

# Sample Input 1:
# Как же я люблю **Markdown**!

# Sample Output 1:
# Как же я люблю <strong>Markdown</strong>!

# Sample Input 2:
# А тут и **Bold text**, и *Italic*!

# Sample Output 2:
# А тут и <strong>Bold text</strong>, и <em>Italic</em>!

# Sample Input 3:
# *Курсив* и **Жирный текст**

# Sample Output 3:
# <em>Курсив</em> и <strong>Жирный текст</strong>


import re

def process(match_obj):
    key, text = match_obj.groups()
    return {'**': r'<strong>{}</strong>', '*': r'<em>{}</em>'}.get(key).format(text)

print(re.sub(r'(\*{1,2})(.*?)\1', process, input()))