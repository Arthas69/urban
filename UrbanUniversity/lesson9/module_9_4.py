from random import choice

# Lambda functions
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))

print(result)
# print([False, True, True, False, False, False, False, False, True, False, False, False, False, False])


# Closures
def get_advanced_writer(filename):

    def write_everything(*data):
        with open(filename, 'w') as f:
            for item in data:
                f.write(str(item) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Class call
class MysticBall(object):
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
