def print_params(a=1, b='строка', c=True):
    return a, b, c


print('With and without params')
print(print_params())
print(print_params(a=10))
print(print_params(a=10, b='string'))
print(print_params(a=10, b='word', c=False))

print('Params from task')
print(print_params(b=25))
print(print_params(c=[1,2,3]))


values_list = [5, 'string', True]
values_dict = {'a': 5, 'b': 'string', 'c': True}

print('Unpacking below')
print(print_params(*values_list))
print(print_params(**values_dict))


values_list_2 = [54.32, 'Строка']
print('Unpacking with 2 parameters below')
print(print_params(*values_list_2, 42))
