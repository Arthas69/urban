# DICTIONARY

# Create dict
my_dict = {'name': 'Eduard', 'age': 35}
print('Dict:', my_dict)

# Get value with an existing key
name = my_dict['name']

# Try to get non-existing key-value
is_student = my_dict.get('is_student', False)

# Print
print('Existing value:', name)
print('Non-existing value:', is_student)

# Update dict with two new pairs
my_dict.update({'is_student': True, 'language': 'Python'})
print('Modified dictionary:', my_dict)

# Delete pair from dict, and save its value in var
language = my_dict.pop('language')
print('Deleted value:', language)

print('Final dict:', my_dict)

# SET

# Create set
my_set = {1, 2, 33, 5.8, 'string', True, (1, 2, 3), 1, 2, 5}
print('Set:', my_set)

# Update set with elements
my_set |= {8, 6}
# my_set.update({8, 6})
# my_set.add(8)
# my_set.add(6)
print('Modified set:', my_set)

# Delete element from set
my_set.discard('string')
# my_set.remove('string')
# my_set.pop()
print('Value was discarded:', my_set)
