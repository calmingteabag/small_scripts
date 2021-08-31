long_months = [1, 3, 5, 7, 8, 10, 12]
short_months = [4, 6, 9, 11]
day_interval = ''


def check_day():
    day = input("Digite o dia do mês: ")

    while True:
        if day.isdigit() is True:
            return day
            break

        else:
            print("Somente digitos")
            day = input("Digite novamente o dia do mês: ")
            continue


def check_month():
    mes = input("Digite o mês: ")

    while True:
        if mes.isdigit() is True and 1 <= int(mes) <= 12:
            return mes
            break
        else:
            print("Somente digitos e valores entre 1 e 12")
            mes = input("Digite novamente o mês: ")
            continue


def check_year():
    ano = input("Digite o ano: ")

    while True:
        if ano.isdigit() is True and 1850 <= int(ano) <= 2021:
            return ano
            break
        else:
            print("Somente digitos e ano entre 1850 e 2021")
            ano = input("Digite novamente o ano: ")
            continue


dia = check_day()
mes = check_month()

long_months = [1, 3, 5, 7, 8, 10, 12]
short_months = [4, 6, 9, 11]
day_interval = ''

ano = check_year()

while True:
    if int(mes) in long_months:
        day_interval = 31
        if 1 <= int(dia) <= 31:
            print("Valid day")
            break
        else:
            print("O mês escolhido tem 31 dias, escolha outro numero entre 1 e 31")
            dia = check_day()
            continue

    elif int(mes) in short_months:
        day_interval = 30
        if 1 <= int(dia) <= 30:
            print("Valid day")
            break
        else:
            print("O mês escolhido tem 30 dias, escolha outro numero entre 1 e 30")
            dia = check_day()
            continue

    else:
        day_interval = 28
        if 1 <= int(dia) <= 28:
            print("Valid day")
            break
        else:
            print(f"{dia} é um dia invalido para o mês de Fevereiro")
            dia = check_day()
            continue




print(f"O ano {dia} / {mes} / {ano} é uma data valida.")
