from math import sqrt
import itertools

message = ('Добро пожаловать в самую лучшую программу для вычисления ' 
           'квадратного корня из заданного числа')
print(message)


def CalculateSquareRoot(number):
    """ Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number):
    if your_number<= 0:
        return
     
    root = 0
    print(f'Мы вычислили квадратный корень'
          f' из введённого вами числа.'
          f' Это будет: {CalculateSquareRoot(your_number)}')


print(message)
calc(25.5)