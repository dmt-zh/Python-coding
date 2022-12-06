# Напишите программу, которая заменит am на pm, а pm на am.

# Sample Input 1:
# It's already 12:00am and I still don't want to sleep.

# Sample Output 1:
# It's already 12:00pm and I still don't want to sleep.

# Sample Input 2:
# 2:00 am 3:00 pm 10:00 pm 3:00 am 1:00 am  5:00 am 8:00 am 7:00 am 5:00 pm 8:00 pm 7:00 pm 6:00 pm
# 11:00 am 4:00 am 9:00 pm 6:00 am 12:00 am 12:00 pm 9:00 am 1:00 pm 11:00 pm 4:00 pm 2:00 pm 10:00 am

# Sample Output 2:
# 2:00 pm 3:00 am 10:00 am 3:00 pm 1:00 pm  5:00 pm 8:00 pm 7:00 pm 5:00 am 8:00 am 7:00 am 6:00 am 11:00 pm
# 4:00 pm 9:00 am 6:00 pm 12:00 pm 12:00 am 9:00 pm 1:00 am 11:00 am 4:00 am 2:00 am 10:00 pm

# Sample Input 3:
# pm am pm

# Sample Output 3:
# am pm am



import re

def process(match_obj):
    value = match_obj[0]
    return 'pm'if value == 'am' else 'am'


processed = re.sub(r'(am|pm)', process, input())
print(processed)