# Code returns a roman numeral based on input
# Limited to positive years up to 9999

def number_romanization():

    # Limits the usr input to specified constraints (positive, only integers, non zero, non negative and
    # up to 4 digits) and to ignore inputs starting with zero (year 0233, 02, etc)
    while True:
        year_input = input("Digite um ano: ")

        if year_input == "0" or year_input == "00" or year_input == "000" or year_input == "0000":
            print("Zeros não são anos válidos")

        elif len(year_input) > 4:
            print("Somente anos de quatro ou menos algarismos são válidos")

        elif year_input.isdigit() == True:
            if len(year_input) > 4:
                print("Somente anos de quatro ou menos algarismos são válidos")
                continue
            if 1 <= len(year_input) <= 4 and year_input[0] == "0":
                print("Anos não começam com zero")
            else:
                break
        else:
            print("Algarismos invalidos")
            continue

    milenium = century = decade = year = ''

    # Creates a variable for the year length (number of digits) and a tuple so
    # it can be divided in decimals later
    year_length = len(str(year_input))
    year_tuple = tuple(str(year_input))

    # Converts each decimal part to roman numerals
    def roman_milenia():
        print_milhares = "M" * milenium
        return print_milhares

    def roman_century():
        if century != 0:
            if 1 <= century <= 3:
                return "C" * century
            if century == 4:
                return "CD"
            if century == 5:
                return "D"
            if 6 <= century <= 8:
                return "D" + ("C" * (century - 5))
            if century == 9:
                return "CM"
        else:
            return ''

    def roman_decade():
        if decade != 0:
            if 1 <= decade <= 3:
                return "X" * decade
            if decade == 4:
                return "XL"
            if decade == 5:
                return "L"
            if 6 <= decade <= 8:
                return "L" + ("X" * (decade - 5))
            if decade == 9:
                return "XC"
        else:
            return ''

    def roman_year():
        if year != 0:
            if 1 <= year <= 3:
                return "I" * year
            if year == 4:
                return "IV"
            if year == 5:
                return "V"
            if 6 <= year <= 8:
                return "V" + ("I" * (year - 5))
            if year == 9:
                return "IX"
        else:
            return ''

    # Return results accordingly to the input length
    if year_length == 4:
        thousands, hundreds, tenths, singles = year_tuple
        milenium = int(thousands)
        century = int(hundreds)
        decade = int(tenths)
        year = int(singles)

        # print(roman_milenia() + roman_century() + roman_decade() + roman_year())
        return roman_milenia() + roman_century() + roman_decade() + roman_year()

    elif year_length == 3:
        hundreds, tenths, singles = year_tuple
        century = int(hundreds)
        decade = int(tenths)
        year = int(singles)

        # print(roman_century() + roman_decade() + roman_year())
        return roman_century() + roman_decade() + roman_year()

    elif year_length == 2:
        tenths, singles = year_tuple
        decade = int(tenths)
        year = int(singles)

        # print(roman_decade() + roman_year())
        return roman_decade() + roman_year()

    else:
        year = int(year_input)

        # print(roman_year())
        return roman_year()


# Code to print the result
ask_continue = ''
while True:

    if ask_continue == 'done':
        break
    else:
        print(f" O ano que você digitou é escrito como {number_romanization()} em algarismos romanos.")
        ask_continue = input("Deseja continuar? ")
