""" A program asks the user for a price and outputs only the dollar value,
e.g. when input is $2.65 -> 2 will be printed to the screen.
"""


def GetPrice():
    """Asks the user for a price.
    Input: a number.
    """
    while True:
        price = input("Please, give me the price in a format $2.65.\n")

        if price[0] != '$':
            print("Please, check the format, it should be as in the example: $2.65.\n")
        else:
            price_number = price[1:]
            try:
                price_number = float(price_number)
            except ValueError:
                print("The price should be a number.\n")
            else:
                return price_number


def main():
    price = GetPrice()
    from math import floor
    print("The dollar value of the price input is " + str(floor(price)))


main()
