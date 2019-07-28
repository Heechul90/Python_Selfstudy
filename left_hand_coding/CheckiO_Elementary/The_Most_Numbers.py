### The_Most_Numbers

def the_most_numbers(*args):
    if args:                    # 값이 하나라도 있으면 True가 된다.
        return max(args) - min(args)

    else:
        return 0


the_most_numbers(1, 2, 3)
the_most_numbers(-99.9, 99.9)
the_most_numbers(1, 1)
the_most_numbers(0, 0)
the_most_numbers(1, 2, 99)
the_most_numbers(1, 2, 3.5, 95.3)
