
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__()
# для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        for row in self.lst:
            for i in row:
                print(f'{i:4}', end='')
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.lst)):
            for g in range(len(other.lst[i])):
                self.lst[i][g] = self.lst[i][g] + other.lst[i][g]
        return Matrix.__str__(self)


matrix = Matrix([[3, 3, 1], [2, 2, 1], [4, 4, 1], [5, 5, 1]])
matrix2 = Matrix([[6, 6, 2], [7, 7, 2], [8, 8, 2], [9, 9, 2]])
print(matrix.__add__(matrix2))


# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, sizes):
        self.sizes = sizes

    @property
    def expense(self):
        return f'textile_spent: {self.sizes / 6.5 + 0.5 + 2 * self.sizes + 0.3  :.2f)}'

    @abstractmethod
    def abstract(self):
        return 'abstract'


class Coat(Clothes):
    def consumption(self):
        return f'For coat: {self.sizes / 6.5 + 0.5 :.2f} textile'

    def abstract(self):
        return 'abstract'


class Suit(Clothes):
    def consumption(self):
        return f'For suit: {2 * self.sizes + 0.3 :.2f} textile'

    def abstract(self):
        pass


coat = Coat(400)
suit = Suit(55)
clothes = Clothes
print(coat.consumption())
print(suit.consumption())


# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как произведение количества ячеек этих двух клеток.

# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
# деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду —
# 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'SUM: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'MINUS: {sub}' if sub > 0 else 'SIZE < 0'

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(22)
cell_2 = Cell(4)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(9))
