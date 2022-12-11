def fizzbuzz(liczba):
    if liczba %3 == 0 and liczba %5 == 0:
        return "fizzbuzz"
    elif liczba %3 == 0:
        return "fizz"
    elif liczba %5 == 0:
        return "buzz"
    return liczba
