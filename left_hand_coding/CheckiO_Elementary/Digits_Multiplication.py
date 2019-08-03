### Digits_Multiplication



def digits_multiplication(number):
    res =1

    for d in str(number):
        if int(d):
            res = res * int(d)

    return res

digits_multiplication(18009)
digits_multiplication(123405)
digits_multiplication(999)
digits_multiplication(100004)