"""A program asks the user for their height: first - for the height portion in feet, and then - for the inches one.
After it converts the height to meters.
1m = 39.3701in
1foot = 12in
"""


def AskForHeight(unit):
    """Asks user for their height.
    """
    while True:
        height = input("What is your height, please, write only " + unit + " portion?\n")
        try:
            height = int(height)
        except ValueError:
            print ("Please, write your height using whole numbers.\n")
            continue
        else:
            return height


def ConvertToMeters(height_feet, height_inches):
    """Converts feets and inches into meters.
    Input:integer.
    """
    feet_to_inches = height_feet*12
    height_inches += feet_to_inches
    height_meters = height_inches / 39.3701
    return height_meters


def main():
    height_feet = AskForHeight('FEET')
    height_inches = AskForHeight('INCHES')
    height_meters = ConvertToMeters(height_feet, height_inches)
    height_meters = str(round(height_meters, 2))
    print("Your height in meters is", height_meters, "m.")


main()









