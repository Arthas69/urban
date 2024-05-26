immutable_var = (1, 'string', 5.5, True)
print(immutable_var)

new_immutable_var = immutable_var + ('new_item',)
print(new_immutable_var)

# immutable_var[0] = 100  # приведет к ошибке TypeError
# Попытка изменить элемент кортежа по индексу не сработает и выкинет ошибку, так как кортеж является неизменяемым объектом,
# но кортежи можно складывать. Если к одному кортежу, применив оператор + или *, прибавить другой кортеж, то будет создан новый
# кортеж, который будет включать в себя элементы обоих кортежей

mutable_list = [2, 'word', 3.5, False]
print(mutable_list)

mutable_list[-1] = True
print(mutable_list)
