# Получите все числовые значения, после которых идёт знак ₽. Значения с неразрывным пробелом &nbsp; игнорируем.

# Sample Input 1:
# <div class="main-indicator_rates"><div class="main-indicator_rates-table"><div class="main-indicator_rates-head">
# <div class="col-md-2 col-xs-7"><a href="/currency_base/">Курсы валют</a></div><div class="col-md-2 col-xs-7 _right">
# <a href="/currency_base/daily/?UniDbQuery.Posted=True&amp;UniDbQuery.To=22.04.2022">22.04.2022</a></div>
# <div class="col-md-2 col-xs-7 _right"><a href="/currency_base/daily/?UniDbQuery.Posted=True&amp;UniDbQuery.
# To=23.04.2022">23.04.2022</a></div></div><div class="main-indicator_rate"><div class="col-md-2 col-xs-9 _dollar">
# USD</div><div class="col-md-2 col-xs-9 _right mono-num">74,9990 ₽</div><div class="col-md-2 col-xs-9 _right
# mono-num">73,5050 ₽</div><div class="main-indicator_tooltip" id="V_R01235"><div class="main-indicator_tooltip-head">
# <button class="main-indicator_tooltip-head-btn _left "></button><div class="main-indicator_tooltip-head-text">
# 19.04.2022 - 23.04.2022</div><button class="main-indicator_tooltip-head-btn _right _disabled "></button></div>
# <table class="main-indicator_tooltip-table"><tr><td class="_day">вт</td><td class="_date">19.04</td><td>79,4529&nbsp;₽
# </td><td class="_green">-0,5908&nbsp;₽</td></tr><tr><td class="_day">ср</td><td class="_date">20.04
# </td><td>79,0287&nbsp;₽</td><td class="_green">-0,4242&nbsp;₽</td></tr><tr><td class="_day">чт</td>
# <td class="_date">21.04</td><td>77,0809&nbsp;₽</td><td class="_green">-1,9478&nbsp;₽</td></tr><tr><td class="_day">
# пт</td><td class="_date">22.04</td><td>74,9990&nbsp;₽</td><td class="_green">-2,0819&nbsp;₽</td></tr><tr><td class="_day">
# сб</td><td class="_date">23.04</td><td>73,5050&nbsp;₽</td><td class="_green">-1,4940&nbsp;₽</td></tr></table>
# <div class="main-indicator_tooltip-footer">Официальный курс Банка России</div></div></div><div class="main-indicator_rate">
# <div class="col-md-2 col-xs-9 _euro">EUR</div><div class="col-md-2 col-xs-9 _right mono-num">81,2239 ₽</div><div
# class="col-md-2 col-xs-9 _right mono-num">80,0249 ₽</div><div class="main-indicator_tooltip" id="V_R01239">
# <div class="main-indicator_tooltip-head"><button class="main-indicator_tooltip-head-btn _left ">
# </button><div class="main-indicator_tooltip-head-text">19.04.2022 - 23.04.2022</div><button class=
# "main-indicator_tooltip-head-btn _right _disabled "></button></div><table class="main-indicator_tooltip-table">
# <tr><td class="_day">вт</td><td class="_date">19.04</td><td>86,4289&nbsp;₽</td><td class="_green">-0,6426&nbsp;₽
# </td></tr><tr><td class="_day">ср</td><td class="_date">20.04</td><td>85,9674&nbsp;₽</td><td class="_green">
# -0,4615&nbsp;₽</td></tr><tr><td class="_day">чт</td><td class="_date">21.04</td><td>83,2705&nbsp;₽</td><td
# class="_green">-2,6969&nbsp;₽</td></tr><tr><td class="_day">пт</td><td class="_date">22.04</td><td>81,2239&nbsp;₽
# </td><td class="_green">-2,0466&nbsp;₽</td></tr><tr><td class="_day">сб</td><td class="_date">23.04
# </td><td>80,0249&nbsp;₽</td><td class="_green">-1,1990&nbsp;₽</td></tr></table><div class="main-indicator_tooltip
# -footer">Официальный курс Банка России</div></div></div></div><a class="main-indicator_rates-link"
# href="/key-indicators/">Все показатели</a></div>

# Sample Output 1:
# 74,9990 ₽
# 73,5050 ₽
# 81,2239 ₽
# 80,0249 ₽



import re
words = re.finditer(r'(?:[\d+\,]+\d+)\s₽', input())
print(*(w.group() for w in words), sep='\n')