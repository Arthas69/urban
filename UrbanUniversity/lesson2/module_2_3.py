my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0

while i < len(my_list):
    el = my_list[i]

    if el > 0:
        print(el)
    elif el < 0:
        break

    i += 1
