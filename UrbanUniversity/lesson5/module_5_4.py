class House(object):
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        if isinstance(value, int):
            if self.floors >= value:
                self.floors -= value
            else:
                print("Not enough floors")
        return self

    def __rsub__(self, value):
        return self.__sub__(value)

    def __isub__(self, value):
        return self.__sub__(value)

    def __mul__(self, value):
        if isinstance(value, int):
            self.floors *= value
        return self

    def __rmul__(self, value):
        return self.__mul__(value)

    def __imul__(self, value):
        return self.__mul__(value)

    def __truediv__(self, value):
        print("Invalid operation")
        return self

    def __itruediv__(self, value):
        return self.__truediv__(value)

    def __rtruediv__(self, value):
        return self.__truediv__(value)

    def __floordiv__(self, value):
        return self.__truediv__(value)

    def __rfloordiv__(self, value):
        return self.__truediv__(value)

    def __ifloordiv__(self, value):
        return self.__truediv__(value)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        else:
            return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        else:
            return False

    def __len__(self):
        return self.floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.floors}"

    def __del__(self):
        print(f"{self.name} снесен, но он остается в истории")

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
