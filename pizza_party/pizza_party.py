"""A program helps to plan if you can have a party or not.
First it asks the user for the number of people that will attend a party.
Also  the number of drinks you will provide and the number of pizzas.
And finally it helps to determine if you can have the party or not.
The criteria is the following: four drinks minimum and one quarter of a pizza for each guest.
"""


def AskNumberPeople():
    """Asks the user for the number of people that will attend a party.
    Input: integer."""
    while True:
        num_people = input("How many people will attend a party?\n")
        try:
            num_people = int(num_people)
        except ValueError:
            print("The number of guests should be an integer.\n")
        else:
            return num_people


def AskAvailableTreats(unit):
    """Asks how many of each treat is available for the party.
    Input: number."""
    while True:
        value = input("How many of " + unit + " there are for the party?\n")
        try:
            value = float(value)
        except ValueError:
            print("Please, enter the number of " + unit + " you plan to provide.\n")
        else:
            return value


def DeterminePartyOrNot(num_people, num_drinks, num_pizzas):
    """Determines if you can have a party.
    Four drinks minimum for each guest.
    One quarter of a pizza for each guest.
    """
    if num_drinks/num_people >= 4 and num_pizzas/num_people >= 0.25:
        return True
    else:
        return False


def main():
    num_people = AskNumberPeople()
    num_drinks = AskAvailableTreats('drinks')
    num_pizzas = AskAvailableTreats('pizzas')
    if DeterminePartyOrNot(num_people, num_drinks, num_pizzas):
        print("There will be a party! \n"
              "You have " + str(round(num_drinks/num_people)) + " drinks for each guest \n"
              "and " + str(round(num_drinks/num_people)) + " quarters of pizza!")
    else:
        print("It looks like there will be no party this time.")


if __name__ == "__main__":
    main()







