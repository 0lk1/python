"""
The program asks the user to input the names of cities they would like to visit.

The program should then print two sentences, e.g.:

'You would like to visit Tel Aviv as city 1	and	Haifa as city 2	and Negev as city 3	on your trip.'
'You would like to visit Tel Aviv as city 2 and Haifa as city 3 and Negev as city 4 on your trip.'
"""


def AskForNumberCities():
    """Asks the user to enter the number of cities they want to visit
    """
    while True:
        number_cities = input("How many cities you would like to visit on your trip?\n")
        try:
            number_cities = int(number_cities)
        except ValueError:
            print("The number of cities should be an integer, please, try again.")
            continue
        else:
            return number_cities


def AskForCityName(number_cities):
    """Asks the user to enter the cities they want to visit. Doesn't allow to enter the same city twice.
    """
    city_list = []
    while len(city_list) < number_cities:
        city = input("What city you would like to visit?\n")
        if city in city_list:
            print ("You have already entered this city, please, try another one.")
            continue
        else:
            city_list.append(city)
    return city_list


def PrintFirstCitySentence(city_list):
    """Prints the sentence with cities provided and their indexes.
    """
    sentence = ""
    sentence += "You would like to visit"
    for i, item in enumerate(city_list):
        sentence += ' ' + item + " as city " + str(i+1)
    sentence += " on your trip."
    print (sentence)
    return sentence


def PrintAddOneCityNumSentence(sentence):
    """Adds 1 to every digit in a sentence.
    """
    words = sentence.split(' ')
    sentence = ""
    for w in words:
        if w.isdigit():
            sentence += " " + str(int(w) + 1)
        else:
            sentence += " " + w
    sentence = sentence[1:]
    print (sentence)
    return sentence


def main():
    number_cities = AskForNumberCities()
    city_list = AskForCityName(number_cities)
    print("\n")
    sentence = PrintFirstCitySentence(city_list)
    PrintAddOneCityNumSentence(sentence)


main()
