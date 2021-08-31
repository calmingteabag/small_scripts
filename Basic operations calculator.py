# This is a very basic calculator that picks two inputs an operator
# and returns a result on a txt file

def input_one():
    while True:
        input_a = input("Valor A? ")

        try:
            int(input_a)

        except:
            print("Somente numeros")
            continue
        break

    usr_input_a = int(input_a)
    return usr_input_a


def input_two():
    while True:
        input_b = input("Valor B? ")

        try:
            int(input_b)

        except:
            print("Somente numeros")
            continue
        break

    usr_input_b = int(input_b)
    return usr_input_b


def write_to_txt():
    with open("/receipt.txt", 'a') as receipt:
        receipt.write("\n" + str(value_a) + "\n" + usr_op + "\n" + str(value_b) + "\n" + "= " + str(usr_result))


ask_continue = ""
usr_op = ""

while True:

    operations = ["+", "-", "/", "*"]
    usr_op = input("Qual operação? ")

    if usr_op in operations:

        # soma

        if usr_op == "+":

            value_a = input_one()
            value_b = input_two()

            usr_result = value_a + value_b
            print(usr_result)
            write_to_txt()

            ask_continue = input("Done? ")
            if ask_continue == "done":
                break
            else:
                continue
        # subtração

        elif usr_op == "-":

            value_a = input_one()
            value_b = input_two()

            usr_result = value_a - value_b
            print(usr_result)
            write_to_txt()

            ask_continue = input("Done? ")
            if ask_continue == "done":
                break
            else:
                continue
        # divisão

        elif usr_op == "/":

            value_a = input_one()

            while True:
                value_b = input_two()
                check_zero = 0

                if value_b == 0:
                    print("Não se divide por zero")
                    continue
                else:
                    break

            usr_result = value_a / value_b
            print(usr_result)
            write_to_txt()

            ask_continue = input("Done? ")
            if ask_continue == "done":
                break
            else:
                continue

        # multiplicação

        elif usr_op == "*":

            value_a = input_one()
            value_b = input_two()

            usr_result = value_a * value_b
            print(usr_result)
            write_to_txt()

            ask_continue = input("Done? ")
            if ask_continue == "done":
                break
            else:
                continue

    else:
        print("Operador inválido")
        continue

    break
