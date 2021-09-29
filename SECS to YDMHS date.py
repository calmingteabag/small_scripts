# Solved this cata in codewars and thought it was nice to have a function of this around

def secs_to_galaxy():

    seconds = ''
    usr_input = ''

    while True:
        """
        The usual check to see if user input is a number and not
        a random gibberish
        """
        if usr_input.isdigit():
            seconds = int(usr_input)
            break
        else:
            usr_input = input("Typer a time in seconds: ")
            continue

    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 365)

    return sec, min, hour, day, year


secs_to_galaxy()
