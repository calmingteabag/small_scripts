word = 'filha'
usrword = 'sabia'

for pos, letter in enumerate(usrword):
    if letter not in word:
        print('red')
    elif usrword[pos] != word[pos]:
        print('yellow')
    else:
        print('green')
