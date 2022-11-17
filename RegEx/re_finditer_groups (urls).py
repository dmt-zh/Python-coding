# Напишите программу, которая будет находить ссылки с помощью re.finditer, и разделять их на части:
# протокол, адрес, параметры, якорь. Протокол и адрес у ссылок есть всегда.

# Sample Input 1:
# В этом https://stepik.org/lesson/704265/step/2?unit=704697#test тексте https://example.com/ очень
# многоhttps://keep.google.com/#homeразных http://oldastoundingrelaxedlaugh.neverssl.com/onlineссылок.

# Sample Output 1:
# Полная ссылка: https://stepik.org/lesson/704265/step/2?unit=704697#test
# Протокол: https | Домен: stepik.org | Параметры: ?unit=704697 | Якорь: #test

# Полная ссылка: https://example.com/
# Протокол: https | Домен: example.com | Параметры: None | Якорь: None

# Полная ссылка: https://keep.google.com/#home
# Протокол: https | Домен: keep.google.com | Параметры: None | Якорь: #home

# Полная ссылка: http://oldastoundingrelaxedlaugh.neverssl.com/online
# Протокол: http | Домен: oldastoundingrelaxedlaugh.neverssl.com | Параметры: None | Якорь: None


import re

class RawURLsHandler:
    def __init__(self, regexp=None):
        if regexp:
            self._patt = regexp
        else:
            self._patt = r'(?P<href>(?P<http>htt[ps]*):\/\/(?P<domain>[a-z.\d]*?)\/[a-z\/\d_-]*(?P<args>\?[^#\s]*)?(?P<ancor>[#][a-z]*)?)'
        self._attr_names = ('href', 'http', 'domain', 'args', 'ancor')
        self._text_names = ('Полная ссылка', 'Протокол', 'Домен', 'Параметры', 'Якорь')

    def __call__(self, raw_text, *args, **kwargs):
        iterator = re.finditer(self._patt, raw_text)
        for data in iterator:
            attrs = data.groupdict()
            lst = [f'{v}: {attrs.get(k)}' for k, v in zip(self._attr_names, self._text_names)]
            url, args = lst[0], lst[1:]
            out = f'{url}\n{" | ".join(args)}\n'
            print(out)


get_urls = RawURLsHandler()
get_urls(input())