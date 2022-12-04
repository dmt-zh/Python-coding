# mm/dd/yyyy на dd/mm/yyyy
# Все даты в примерах - даты формата mm/dd/yyyy, замените их на dd/mm/yyyy.
# Для разделителей используются символы . и /. Их трогать не нужно.

# Sample Input 1:
# Сегодня 04/24/2022.

# Sample Output 1:
# Сегодня 24/04/2022.

# Sample Input 2:
# Ловите дату, разделённую точками: 01.22.2089.

# Sample Output 2:
# Ловите дату, разделённую точками: 22.01.2089.


import re

processed = re.sub(r'(\d{2})(.)(\d{2})', r'\3\2\1', input())
print(processed)