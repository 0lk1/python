"""
A program asks to give it a letter to determine if the letter is a vowel or not.
"""


def AskForLetter():
    """Repeatedly ask the user for a single letter until the user types "quit" to exit the program or entered a vowel.
    Input: letter, letters, any symbols or quit.
    """
    while True:
        letter = input("Please, give me any letter to guess if it is a vowel or type 'quit' to end!\n")
        letter = str(letter)
        letter_len = len(letter)

        if letter == 'quit':
            break
        elif letter_len != 1:
            print (letter, "is not a single letter. Try again.")
            continue

        result = IsVowel(letter)
        PrintIsVowel(letter, result)


def IsVowel(letter):
    """Takes as input a variable called letter and determines if it is a vowel or not.
    If a vowel - returns True, and if not a vowel - returns to determine if letter is vowel or not.
    """
    return IsUppercaseVowel(letter) or IsLowercaseVowel(letter)


def IsLowercaseVowel(letter):
    """Takes a single variable as input called letter and returns True if the letter is a lowercase vowel or False if not.
    """
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return True
    else:
        return False

def IsUppercaseVowel(letter):
    """Takes a single variable as input called letter and returns True if the letter is an uppercase vowel or False if not.
    """
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        return True
    else:
        return False


def PrintIsVowel(letter, result):
    """Prints a sentence to the user indicating if the input is a vowel or not.
    """
    if result:
        print ("You entered a vowel letter ", letter, "!")
        exit(0)
    else:
        print ("You entered", letter, ", and it is NOT a vowel!")


AskForLetter()




