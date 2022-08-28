# 2) Создайте класс «Правильная дробь» и реализуйте методы сравнения,
# сложения, вычитания и произведения для экземпляров этого класса.

from __future__ import annotations


class ProperFraction:
    def __init__(self, numerator: int, denominator: int):
        if numerator >= denominator:
            raise TypeError("The numerator must be less than the denominator\n")
        if denominator == 0:
            raise ZeroDivisionError("The denominator must not be 0\n")
        self.numerator = numerator
        self.denominator = denominator

    def calculation_fraction(self):
        return self.numerator / self.denominator

    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'

    def __eq__(self: ProperFraction, other: ProperFraction) -> bool:
        return self.calculation_fraction() == other.calculation_fraction()

    def __ne__(self: ProperFraction, other: ProperFraction) -> bool:
        return self.calculation_fraction() != other.calculation_fraction()

    def __gt__(self: ProperFraction, other: ProperFraction) -> bool:
        return self.calculation_fraction() > other.calculation_fraction()

    def __lt__(self: ProperFraction, other: ProperFraction) -> bool:
        return self.calculation_fraction() < other.calculation_fraction()

    def __ge__(self: ProperFraction, other: ProperFraction) -> bool:
        return self.calculation_fraction() >= other.calculation_fraction()

    def __le__(self: ProperFraction, other: ProperFraction) -> bool:
        return self.calculation_fraction() <= other.calculation_fraction()

    def common_denominator(self: ProperFraction, other: ProperFraction) -> int:
        i = other.numerator * 2
        while True:
            if (i % self.denominator) == 0 and (i % other.denominator) == 0:
                return int(i)
            i += 1

    def __add__(self: ProperFraction, other: ProperFraction) -> ProperFraction:
        if self.denominator == other.denominator:
            return ProperFraction((self.numerator + other.numerator), self.denominator)
        common_d = self.common_denominator(other)
        tmp = ((common_d // self.denominator) * self.numerator) + ((common_d // other.denominator) * other.numerator)
        return ProperFraction(tmp, common_d)

    def __sub__(self: ProperFraction, other: ProperFraction) -> ProperFraction:
        if self.denominator == other.denominator:
            return ProperFraction((self.numerator - other.numerator), self.denominator)
        else:
            common_d = self.common_denominator(other)
            tmp = ((common_d // self.denominator) * self.numerator) - ((common_d // other.denominator) * other.numerator)
            return ProperFraction(tmp, common_d)

    def __mul__(self: ProperFraction, other: ProperFraction) -> ProperFraction:
        return ProperFraction(self.numerator * other.numerator, self.denominator * other.denominator)


try:
    fr_1 = ProperFraction(-1, 0)
    fr_2 = ProperFraction(3, 9)
    fr_3 = ProperFraction(2, 2)
except (TypeError, ZeroDivisionError) as err:
    print(err)

print(fr_1 > fr_2)
