import pizza_party


def main():
    res = pizza_party.AskNumberPeople()
    assert type(res) is int
    assert res > 0, "Should be a integer, > 0"

    res = pizza_party.AskAvailableTreats("test-unit")
    assert type(res) is float
    assert res >= 0

    res = pizza_party.DeterminePartyOrNot(10, 10, 10)
    assert res is False,"Incorrect return"
    res = pizza_party.DeterminePartyOrNot(-1, -1, -1)
    assert res is False, "No minus results"


if __name__ == "__main__":
    main()







