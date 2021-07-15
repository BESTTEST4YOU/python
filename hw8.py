# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def string(cls, string_date):
        day, month, year = map(int, string_date.split('-'))
        date1 = cls(day, month, year)
        print(*string_date)
        return date1

    @staticmethod
    def valid_date(string_date):
        day, month, year = map(int, string_date.split('-'))
        day = int(input())
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 3999:
            print(*string_date)
            return day, month, year
        else:
            print('Error')


d = '11-07-2021'
date = Date.string(d)
second_date = Date.valid_date(d)

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class Exception_D(Exception):

    def division_by_zero(self):
        while True:
            a = int(input('Input first number: '))
            b = int(input('Input second number: '))
            try:
                res = round(a / b, 1)
            except ZeroDivisionError:
                print(f"{a} / {b} -  division by 0 is not possible\n")
            else:
                print(f"{a} / {b} = {res} \n")


n = Exception_D()
n.division_by_zero()


# # 3. Создайте собственный класс-исключение, который должен проверять содержимое
# # списка на наличие только чисел. Проверить работу исключения на реальном примере.
# # Необходимо запрашивать у пользователя данные и заполнять список.
# # Класс-исключение должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду
# “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только
# числа и строки. При вводе пользователем очередного элемента необходимо
# реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class MyExcept:
    def __init__(self, *args):
        self.lst = []

    def input_number(self):
        print('Input the numbers through the "ENTER":')
        while True:
            try:
                res = int(input())
                self.lst.append(res)
                print(f'List - {self.lst}')
            except ValueError:
                print(f'Not a number')
                stop = input(f'Continue? Y/N \n').upper()
                if stop == 'Y':
                    print(n.input_number().upper())
                elif stop == 'N':
                    return f'END'


n = MyExcept()
print(n.input_number())

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым для
# классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

    def __str__(self):
        return "\tbrand: {} \tID: {}".format(self.brand, self.id)


class PC(OfficeEquipment):
    amount_sc = 0

    def __init__(self, brand, id, wifi):
        super().__init__(brand, id)
        self.wifi = wifi
        PC.amount_sc += 1

    @staticmethod
    def name():
        return 'PC'

    def wifi(self):
        return self.wifi

    def __str__(self):
        return "\tbrand: {} \tID: {} \tWi-Fi: {}".format(self.brand, self.id, self.wifi)


class Projector(OfficeEquipment):
    amount_x = 0

    def __init__(self, brand, id, projector_wi_fi):
        super().__init__(brand, id)
        self.projector_wi_fi = projector_wi_fi
        Projector.amount_x += 1

    @staticmethod
    def name():
        return 'Projector'

    def wi_fi_module(self):
        return self.projector_wi_fi

    def __str__(self):
        return "\tbrand: {} \tID: {}   \tWi-Fi: {}".format(self.brand, self.id, self.projector_wi_fi)


p = Mfu('Canon', 'DX C5800')
p2 = Mfu('Canon', 'MF832Cdw')
print(p.name(), p.amount_pr, 'qty.')
print(p.__str__())
print(p2.__str__())

s = PC('ASUS', 'GT15CK-RU018T', 'not')
s2 = PC('ASUS', 'GT15CK-RU018T', 'got')
s3 = PC('ASUS', 'GT15CK-RU018T', 'got')
print(s.name(), s.amount_sc, "qty.")
print(s.__str__())
print(s2.__str__())
print(s3.__str__())

x = Projector('Optoma', 'ZH406-W', 'got')
print(x.name(), x.amount_x, 'qty.')
print(x.__str__())
