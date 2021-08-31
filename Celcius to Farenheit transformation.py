def to_celcius(ask_temperature):
    celcius_temp = ((ask_temperature - 32) * 5) / 9
    return celcius_temp


def to_farenheit(ask_temperature):
    farenheit_temp = ((ask_temperature * 9) / 5) + 32
    return farenheit_temp


while True:
    usr_input = input("To Celcius or to Farenheit? ")

    if usr_input.lower() == "celcius":
        print("Ok, to celcius then")

        ask_temperature = input("Qual valor converter para celcius?: ")

        if ask_temperature.isdigit():
            result_temperature = to_celcius(int(ask_temperature))
            print(result_temperature)

            ask_continue = input("Deseja continuar? ('nope' para sair): ")

            if ask_continue == "nope":
                break
            else:
                continue


    elif usr_input.lower() == "farenheit":
        print("Ok, to farenheit then")

        ask_temperature = input("Qual valor converter para farenheit?: ")

        if ask_temperature.isdigit():
            result_temperature = to_farenheit(int(ask_temperature))
            print(result_temperature)

            ask_continue = input("Deseja continuar? ('nope' para sair): ")

            if ask_continue == "nope":
                break
            else:
                continue

    else:
        print("I don't understand")
        continue

