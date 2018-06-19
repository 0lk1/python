"""The program tosses two coins and when they are the same type, will quit.
"""

import random

TOSS_TYPES = ['Heads', 'Tails']


def TossCoins():
    """Uses random to emulate the toss of the coins.
    """
    coin1 = random.choice(TOSS_TYPES)
    coin2 = random.choice(TOSS_TYPES)
    return CheckIfSame(coin1, coin2)


def CheckIfSame(coin1, coin2):
    if coin1 == coin2:
        return True
    else:
        return False


def main():

    toss_counter = 1

    while True:
        if toss_counter == 1:
            print(toss_counter, "time(s) tossing the coins.")
        if TossCoins() is True:
            print("All coins are the same type.")
            break

        else:
            toss_counter = toss_counter + 1
            print(toss_counter, "time(s) tossing the coins.")


main()

