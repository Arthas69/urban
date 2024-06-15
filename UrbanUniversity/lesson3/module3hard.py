def calculate_sum_of_digits(*struct):
    summ = 0
    for i in struct:
        if isinstance(i, (int, float)):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
        elif isinstance(i, dict):
            summ += calculate_sum_of_digits(*i.items())
        elif isinstance(i, (list, tuple, set)):
            summ += calculate_sum_of_digits(*i)

    return summ


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

list_ = [1, 100, 50]


print(calculate_sum_of_digits(data_structure, list_))
