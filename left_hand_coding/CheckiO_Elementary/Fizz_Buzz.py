### Fizz_Buzz


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'Fizz Buzz'

    elif number % 3 == 0:
        return 'Fizz'

    elif number % 5 == 0:
        return 'Buzz'

    else:
        return str(number)


fizz_buzz(15)
fizz_buzz(6)
fizz_buzz(5)
fizz_buzz(7)
fizz_buzz(45)
fizz_buzz(46)