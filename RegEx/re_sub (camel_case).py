# Преобразуйте CamelCase «Верблюжий регистр» в snake_case «Змеиный регистр».

# Sample Input 1:
# MySendMessage

# Sample Output 1:
# my_send_message

# Sample Input 2:
# RegularExpression

# Sample Output 2:
# regular_expression

# Sample Input 3:
# VUpperCase

# Sample Output 3:
# v_upper_case


import re

regexp = re.compile(r'(?:[A-Z][a-z]*|\d+)')
processed = "_".join(regexp.findall(input())).lower()
print(processed)