'''
Conversor de uma linguiça binaria em palavras

Programa itera cada elemento da lista e vai appendando em uma lista temporaria
Quando o contador chega a 8 (8 = um octeto binario), ele concatena os elementos da lista temporaria,
converte de binario pra ascii e appenda a letra numa outra lista

No final, um join pra juntar as letras e formar uma palavra

'''


salsisha = '0100100001100101011011000110110001101111'

char = []
count = 0
letters = []

for i in salsisha:
    char.append(i)
    count += 1

    if count == 8:
        bin_str = ''.join(char)
        converted_bin = chr(int(bin_str, 2))

        letters.append(converted_bin)
        count = 0
        char = []

print(letters)
word = ''.join(letters)
print(word)
