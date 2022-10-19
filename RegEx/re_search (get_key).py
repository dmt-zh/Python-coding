# Получите ключ t и его значение.

# Sample Input 1:
#
# {"errorCode":909,"errorMessage":"Are you a robot? Please enter the captcha below",
# "errorDescription":null,"logStatus":null,"captcha":"\/captcha\/view?_CAPTCHA&amp;t=0.555555+11232131"}

# Sample Output 1:
# t=0.555555+11232131

# Sample Input 2:
# {"errorCode":909,"errorMessage":"Are you a robot? Please enter the captcha below",
# "errorDescription":null,"logStatus":null,"captcha":"\/captcha\/view?_CAPTCHA&amp;t=0.5553455+184231"}

# Sample Output 2:
# t=0.5553455+184231



import re

def get_t_key(string):
    pattern = r't=0\.\d+\+\d+'
    key = re.search(pattern, string).group()
    return key

print(get_t_key(input().strip()))