### Number_Base


def number_base(str_number, radix):
    try:
        return int(str_number, radix)

    except ValueError:
        return -1



number_base('AF', 16)
number_base('101', 2)
number_base('101', 5)
number_base('Z', 36)
number_base('AB', 10)