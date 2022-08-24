# 1) Создайте класс «Прямоугольник», у которого присутствуют два поля
# (ширина и высота). Реализуйте метод сравнения прямоугольников по
# площади. Также реализуйте методы сложения прямоугольников (площадь
# суммарного прямоугольника должна быть равна сумме площадей
# прямоугольников, которые вы складываете). Реализуйте методы
# умножения прямоугольника на число n (это должно увеличить площадь
# базового прямоугольника в n раз).

from __future__ import annotations

class Rectangle:
    def __init__(self, length: float, width: float):
        if length <= 0 or width <= 0:
            raise TypeError("Одна из сторон меньше или равна 0!")
        self.length = length
        self.width = width

    def get_area(self) -> float:
        return self.length * self.width

    def __str__(self):
        return f'L = {self.length}, W = {self.width}, S = {self.get_area()}'

    def __add__(self: Rectangle, other: Rectangle) -> Rectangle:
        if self.length == other.length:
            return Rectangle(self.length, (self.width + other.width))
        if self.length == other.width:
            return Rectangle(self.length, (self.width + other.length))
        if self.width == other.length:
            return Rectangle(other.length, (self.length + other.width))
        if self.width == other.width:
            return Rectangle((self.length + other.length),self.width)
        else:
            raise TypeError("одна сторона 1го прямоугольника должна быть равна 1 стороне 2го прямоугольника")

    def __eq__(self: Rectangle, other: Rectangle):
        if self.get_area() == other.get_area():
            return 1
        return 0

    def __gt__(self: Rectangle, other: Rectangle):
        if self.get_area() > other.get_area():
            return 1
        return 0

    def __lt__(self: Rectangle, other: Rectangle):
        if self.get_area() < other.get_area():
            return 1
        return 0

    def __ne__(self: Rectangle, other: Rectangle):
        if self.get_area() != other.get_area():
            return 1
        return 0

    def __mul__(self: Rectangle, other: int):
        if not isinstance(other, int):
            return NotImplemented
        if other <= 0:
            raise TypeError("Нельзя умножить прямоугольник на число, которое меньше или равно 0")
        self.length = self.length * other

    def __rmul__(self: Rectangle, other: int):
        if not isinstance(other, int):
            return NotImplemented
        if other <= 0:
            raise TypeError("Нельзя умножить прямоугольник на число, которое меньше или равно 0")
        self.length = self.length * other


try:
    rect_1 = Rectangle(2, 4)
    rect_2 = Rectangle(4, 2)
except TypeError as err:
    print(err)

print(rect_1, rect_2, sep="\n")
print("\n")

try:
    rect_3 = rect_1 + rect_2
    # print(rect_3)
except TypeError as err:
    print(err)

try:
    3 * rect_1
    print(rect_1)
except TypeError as err:
    print(err)



