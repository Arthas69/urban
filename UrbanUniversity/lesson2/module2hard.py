from math import ceil


def gen_password(n):
    result = ''

    for i in range(1, ceil(n / 2)):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result += f'{i}{j}'

    return result


num = int(input('Enter number from 3 to 20 inclusively: '))
password = gen_password(num)
print(password)
