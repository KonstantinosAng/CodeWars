# see 


def get_sum_of_digits(num):
    return sum([int(x) for x in str(num)])

print(get_sum_of_digits(123) == 6)