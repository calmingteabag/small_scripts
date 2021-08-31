import random

start = int(input("Valor inicial? "))
finish = int(input("Valor final? "))
tries = int(input("Quantas tentativas? "))

picked_number = random.randint(start, finish)
guess = 0

while picked_number != guess and tries > 0:
    guess = int(input("Qual é o numero? "))
    if picked_number == guess:
        print("Cê adevinhou! ")
        break

    elif guess > picked_number:
        tries -= 1
        dica = guess - picked_number
        if dica >= 5:
            print("O numero ta alto e vc ta longe")
        else:
            print("O numero ta alto, mas vc ta perto")
    elif guess < picked_number:
        tries -= 1
        dica_2 = picked_number - guess
        if dica_2 >= 5:
            print("O numero ta baixo e vc ta frio")
        else:
            print("O numero ta baixo, mas vc ta perto")
else:
    print("Acabô as tentativa")















