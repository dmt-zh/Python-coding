# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

def minion_game(s):
    vowels = 'AEIOU'
    st = 0
    kv = 0

    for i in range(len(s)):
        if s[i] in vowels:
            kv += len(s) - i
        else:
            st += len(s) - i

    if kv > st:
        print(f'Kevin {kv}')
    elif st > kv:
        print(f'Stuart {st}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)