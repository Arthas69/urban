def get_multiplied_digits(num):
    # If number is less than 10, it has only one digit, so return it.
    if num < 10:
        # if num is 0, return 1, because 0 * anything is 0.
        # if num is any digit other than 0, return that digit.
        return num if num else 1
    str_num = str(num)
    digit = int(str_num[0])
    return digit * get_multiplied_digits(int(str_num[1:]))


result = get_multiplied_digits(40203)
print(result)
