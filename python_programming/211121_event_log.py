# Файл с логом содержит записи о некоторых событиях вида:
# event 3 - 'git log -2'
# event 2 - 'git log'
# event 1 - 'git status'

# Пример нового события:
# git fetch origin

# Дополните лог в файле так, чтобы новое событие было записано вверху. Не забудьте указать порядковый номер события.
# event 4 - 'git fetch origin'
# event 3 - 'git log -2'
# event 2 - 'git log'
# event 1 - 'git status'
# Если файл отсутствует или не содержит записей, начните нумеровать события с 1.

# Sample Input 1:
# event = "git fetch origin"
# file_name = "tmp/git.log"

# Sample Output 1:
# event 4 - 'git fetch origin'
# event 3 - 'git log -2'
# event 2 - 'git log'
# event 1 - 'git status'

# Sample Input 2:
# event = "git fetch origin"
# file_name = "tmp/empty_git.log"

# Sample Output 2:
# event 1 - 'git fetch origin'

import os.path
mode = 'r+' if os.path.exists(file_name) else 'x+'
with open(file_name, mode) as fout:
    lines = fout.readlines()
    last_num = int(lines[0].split()[1]) + 1 if len(lines) > 0 else 1
    fout.seek(0)
    fout.write(f"event {last_num} - '{event}'\n")
    fout.writelines(lines)
