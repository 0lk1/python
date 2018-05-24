"""A program takes a 3 word phrase and then converts the words to Pig Latin.

Rule #1: Pig Latin takes the first letter of a word, puts it at the end, and appends 'ay'.
Test: ' boot' to ' ootbay'

Exception: If the first letter is a vowel, in which case we keep it as it is, and append 'hay' to the end.
Test: ' image' to ' imagehay'.

A program keeps translating 3 word phrases into Pig Latin until the user enters in the phrase QUIT.
"""

VOWELS = ['a', 'e', 'i', 'o', 'u'] # Define a GLOBAL list of VOWELS

def AskUserForSentence():
    """Repeatedly ask the user to enter a sentence with only three words and no numbers or any punctuation.
    To exit program the user types QUIT.

    Input: three words or QUIT.
    """

    while True:
        sentence = input("Please, give me any THREE words to translate them to Pig Latin or type 'QUIT' to exit the program!\n")

        if sentence == 'QUIT':
            break

        print("You entered ", sentence, "! Let's look how it will be in Pig Latin!")

        sentence = LowercaseSentence(sentence)
        word_list = SplitSentenceIntoList(sentence)

        if len(word_list) != 3:
            print ("You need to enter exactly 3 words, please, try again.\n\n")
            continue

        words = ConvertWordToPigLatin(word_list)

        Run(words)

        print ("\n\n")

def LowercaseSentence(text):
    """Lowercases all the input"""
    return text.lower()

def SplitSentenceIntoList(sentence):
    """Transfers string input to list"""
    return sentence.split()

def ConvertWordToPigLatin(word_list):
    """Transfers words to Pig Latin going through each word one by one"""

    result = ''
    for word in word_list:
        if word[0] in VOWELS:
           word = word + 'hay'

        else:
            word = word + word[0] +'ay'
            word = word[1:]

        result = result + word + ' '

    return result

def Run(words):
    print ("In Pig Latin your sentence will be: ", words)

AskUserForSentence()