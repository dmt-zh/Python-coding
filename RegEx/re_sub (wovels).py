# Замените все гласные на восклицательный знак.
# Гласные: aeioyuAEIOUауоыиэяюёеАУОЫИЭЯЮЁЕ

# Sample Input 1:
# Especially this one my kinda favourite, and here we go, you dropped it!

# Sample Output 1:
# !sp!c!!ll! th!s !n! m! k!nd! f!v!!r!t!, !nd h!r! w! g!, !!! dr!pp!d !t!

# Sample Input 2:
# Поставил данную композицию на будильник! Теперь просыпаюсь за час до него,спасибо!

# Sample Output 2:
# П!ст!в!л д!нн!! к!мп!з!ц!! н! б!д!льн!к! Т!п!рь пр!с!п!!сь з! ч!с д! н!г!,сп!с!б!!


import re
res = re.sub('(?i)[aeiouyаеёиоуыэюя]', '!', input())
print(res)