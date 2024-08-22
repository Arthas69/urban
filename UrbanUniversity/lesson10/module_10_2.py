from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, strength):
        super().__init__()
        self.name = name.title()
        self.strength = strength
        self.enemies = 100

    def run(self):
        days = 0
        print(f'{self.name}, you are under attack')
        while True:
            if self.enemies <= 0:
                print(f'{self.name} wins after {days} days!')
                break
            self.enemies -= self.strength
            days += 1
            sleep(1)
            print(f'{self.name} fights for {days}..., {max(self.enemies, 0)} enemies remaining')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

first_knight.start()
second_knight.start()