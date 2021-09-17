# Given a multiline string, create a list of lists — each consisting of all the words
# in a line that have more than three characters.

text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''


res = [[x for x in line.strip().split() if len(x) > 3] for line in text.split('\n')]
print(res)