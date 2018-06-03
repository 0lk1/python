"""If i is from 2 to 78, subtract 2 from i;
if j is not between 10 and 15 but is the number 11, then k equals j times 2;
if k is not equal to 7 and i equals 5 or j is greater than 8, set x equal to 200 divided by k;
if i is the sum of j and k, and j is not equal to sum of i and k, then x equals j times k divided by i.
"""


def GetNumbers(unit):
    """
    Asks to give numbers and checks if they are integers. If not - continues to ask.
    Input: integer.
    """
    while True:
        number = input("Please, give me a number for " + unit + ".\n")
        try:
            number = int(number)
        except ValueError:
            print("Please, give me an integer.")
            continue
        else:
            return number


def CalculateX(i,j,k):
    """Calculates x in the series of if-statements.
    Input: i, j, k - all integers."""
    x = None

    if i >= 2 or i <= 78:
        i = i - 2
        print("i is "+ str(i) + " j is " + str(j) + " and k is " + str(k) + ".\n")

    if not(10 <= j <= 15) or j == 11:
        k = j*2
        print("i is " + str(i) + " j is " + str(j) + " and k is " + str(k) + ".\n")

    if (k != 7 and i == 5) or j > 8:
        x = 200/k
        print("i is " + str(i) + " j is " + str(j) + " and k is " + str(k) + ".\n")

    if i == (j+k) and j != i+k:
        x = k*j/i
        print("i is " + str(i) + " j is " + str(j) + " and k is " + str(k) + ".\n")

    if x is None:
        print("x is x, we cannot find it through numbers you provided.")
        return True

    else:
        print("x is " + str(x) + ". Congratulations!")
        return False


def main():
    while True:

        i = GetNumbers("i")
        j = GetNumbers("j")
        k = GetNumbers("k")
        if not CalculateX(i, j, k):
            break


main()

