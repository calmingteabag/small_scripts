import random

cpu_choices = ["R", "P", "S"]
cpu_value = random.choice(cpu_choices)
jogadas = int(input("Digite quantas jogadas: "))
player_value = input("R, P or S?: ").upper()

score_player = 0
score_cpu = 0

while jogadas > 0:

    if player_value == cpu_value:
        print("Empate")
        score_player += 1
        score_cpu += 1
        jogadas -= 1
        player_value = input("R, P or S?: ").upper()

    elif player_value == "R":
        if cpu_value == "P":
            print("Paper wins Rock")
            score_cpu += 1
            jogadas -= 1
            player_value = input("R, P or S?: ").upper()
        else:
            print("Rock wins over Scissors")
            score_player += 1
            jogadas -= 1
            player_value = input("R, P or S?: ").upper()

    elif player_value == "P":
        if cpu_value == "R":
            print("Paper wins over rock")
            score_player += 1
            jogadas -= 1
            player_value = input("R, P or S?: ").upper()
        else:
            print("Scissors win over paper")
            score_cpu += 1
            jogadas -= 1
            player_value = input("R, P or S?: ").upper()

    elif player_value == "S":
        if cpu_value == "P":
            print("Scissors win over paper")
            score_player += 1
            jogadas -= 1
            player_value = input("R, P or S?: ").upper()
        else:
            print("Rock wins over scissors")
            score_cpu += 1
            jogadas -= 1
            player_value = input("R, P or S?: ").upper()
else:
    result = score_player - score_cpu
    if result == 0:
        print("Tie")
    elif result < 0:
        print("Cpu wins")
    else:
        print("Player wins")