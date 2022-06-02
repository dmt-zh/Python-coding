# You are given an integer N followed by N email addresses.
# Your task is to print a list containing only valid email addresses in lexicographical order.

# Valid email addresses must follow these rules:
# It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores.

# The website name can only have letters and digits.
# The maximum length of the extension is 3.

import re
def fun(s):
    if s.count('@') > 1 or s.count('.') > 1:
        return False

    args = s.replace('@', '.').replace('.', ' ').split()
    if len(args) < 3:
        return False

    is_valid = True
    if len(args[-1]) > 3 or not re.match('^[A-Za-z]*$', args[-1]):
        is_valid = False
    if not re.match('^[A-Za-z0-9_-]*$', args[0]):
        is_valid = False
    if not re.match('^[A-Za-z0-9]*$', args[1]):
        is_valid = False
    return is_valid


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)