# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be
# of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Sample Input 0
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output 0
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        line = input()
        if line.startswith('pr'):
            print(lst)
        else:
            command = [str(i) if i.isalpha() else int(i) for i in line.strip().split()]
            if command[0].startswith('ins'):
                lst.insert(command[1], command[2])
            elif command[0].startswith('rem'):
                lst.remove(command[1])
            elif command[0].startswith('ap'):
                lst.append(*command[1:])
            elif command[0].startswith('s'):
                lst.sort()
            elif command[0].startswith('po'):
                lst.pop()
            elif command[0].startswith('rev'):
                lst.reverse()