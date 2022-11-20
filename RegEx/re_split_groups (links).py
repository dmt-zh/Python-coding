# Разделите параметры по символам ? и &.

# Sample Input 1:
# https://stackoverflow.com/questions/tagged/regex?tab=votes&page=11&pagesize=15

# Sample Output 1:
# ['https://stackoverflow.com/questions/tagged/regex', '?', 'tab=votes', '&', 'page=11', '&', 'pagesize=15']

# Sample Input 2:
# https://www.youtube.com/results?search_query=random+stream&sp=EggIARABGAFAAQ%253D%253D

# Sample Output 2:
# ['https://www.youtube.com/results', '?', 'search_query=random+stream', '&', 'sp=EggIARABGAFAAQ%253D%253D']


import re
res = re.split(r'([?&])', input())
print(res)