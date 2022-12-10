# Исправьте код так, чтобы он заменил все буквы O на X. Новая буква должна быть такого же регистра,
# как и оригинальная.

# Sample Input 1:
# LOST CXNTURY - CYBERSITY | scarlord - FALSE HOPE

# Sample Output 1:
# LXST CXNTURY - CYBERSITY | scarlxrd - FALSE HXPE

# Sample Input 2:
# SHADOWBORN shadowborn

# Sample Output 2:
# SHADXWBXRN shadxwbxrn


import re

def get_x(m):
    return {'o': 'x', 'O':'X'}[m[0]]

print(re.sub(r'(?i)o', get_x, input()))