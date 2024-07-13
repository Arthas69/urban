from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = [1] * self.sides_count
        self.set_sides(*sides)
        self.filled = False

    def __len__(self):
        return sum(self.__sides)

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(colors):
        return all(0 <= color <= 255 for color in colors)

    def set_color(self, *colors):
        if self.__is_valid_color(colors):
            self.__color = list(colors)

    def __is_valid_sides(self, new_sides):
        if (isinstance(self, Cube) and len(new_sides) != 1 or
                isinstance(self, (Triangle, Circle)) and len(new_sides) != self.sides_count):
            return False
        return True

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides) if not isinstance(self, Cube) else list(new_sides) * self.sides_count


class Circle(Figure):
    sides_count = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__radius = self.get_sides()[0] / 2 * pi

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__height = self.__get_height()

    def __get_height(self):
        return 2 * self.get_square() / self.get_sides()[0]

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_volume(self):
        return self.get_sides()[0] ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    #Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

`    # print("Тесты для треугольника")
    # triangle1 = Triangle((222, 35, 130), 1, 2)     # Треугольник должен принимать три стороны
    # triangle2 = Triangle((222, 35, 130), 4, 5, 6)  # Создает треугольник со сторонами 4, 5, 6
    # print(triangle1.get_sides())  # [1, 1, 1]
    # print(triangle2.get_sides())  # [4, 5, 6]`
