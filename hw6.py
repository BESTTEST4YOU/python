# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода
# реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться
# только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    __color = ['RED', 'YELLOW', 'GREEN']

    @staticmethod
    def running():
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


t = TrafficLight()
t.running()

#second var:
from time import sleep
class TrafficLight:
    __color = ['Красный']

    def running(self):
        print('RED')
        sleep(7)
        print('YELLOW')
        sleep(2)
        print('GREEN')
        sleep(3)
traf_light = TrafficLight()
traf_light.running()

#another var:
from time import sleep
class TrafficLight:
    __color = ['RED', 'YELLOW', 'GREEN']

    def running(self):
        print('горит ', self.__color[0])
        sleep(7)
        print('горит ', self.__color[1])
        sleep(2)
        print('горит ', self.__color[2])
        sleep(3)
traf_light = TrafficLight()
traf_light.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании
# экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
# дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self.weight = 25
        self.height = 5
        self._length = length
        self._width = width

    def asphalt_mass(self):
        res = self._length * self._width * self.weight * self.height / 1000
        print(f'Для выполнения работ нужно: {round(res)} асфальта')


r = Road(5000, 20)
r.asphalt_mass()


# second var:

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        return f'Масса равна: {(self._length * self._width * 25 * 0.05) / 1000} т'


road1 = Road(5000, 20)
print(road1.calc())


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


p = Position('Myers', 'Glenford', 'Computer scientist', '100000', '10000')
print(p.get_full_name(), p.get_total_income())

#second var:
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    @property
    def get_total_income(self):
        return f'{sum(self._income.values())}'

worker1 = Position('Myers', 'Glenford', 'Computer scientist', 100000, 10000)
print(worker1.get_full_name(), worker1.get_total_income)

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name}: go.'

    def stop(self):
        return f'\n{self.name}: stopped'

    def turn(self, directions):
        return f'\n{self.name} turned: {directions}'

    def speed(self):
        return f'speed is: {self.speed}'


class TownCar(Car):
    def rspeed(self):
        if self.speed > 61:
            return f'Speed is: {self.speed} - over speed!'
        else:
            return f'Speed is: {self.name} - ok'


class SportCar(Car):
    def rspeed(self):
        if self.speed > 61:
            return f'Speed is: {self.speed} - over speed!'
        else:
            return f'Speed is: ok'


class WorkCar(Car):
    @property
    def rspeed(self):
        if self.speed > 41:
            return f'Speed is: {self.speed} - over speed!'
        else:
            return f'Speed is: ok'


class PoliceCar(Car):
    def rspeed(self):
        if self.speed > 80:
            return f'Speed is: {self.speed} - over speed!'
        else:
            return f'Speed is: ok'


TownCar = TownCar(120, 'asphalt', 'KIA', False)
print('\nTownCar:\n' + TownCar.go(), TownCar.rspeed(), TownCar.turn('left'), TownCar.stop())

SportCar = SportCar(170, 'white', 'Porsche', False)
print('\nSportCar:\n' + SportCar.go(), SportCar.rspeed(), SportCar.turn('right'))

WorkCar = WorkCar(40, 'yellow', 'VW', False)
print('\nWorkCar:\n' + WorkCar.go(), WorkCar.rspeed, WorkCar.turn('left'), WorkCar.stop())

PoliceCar = PoliceCar(80, 'black', 'Ford', True)
print('\nPoliceCar:\n' + PoliceCar.go(), PoliceCar.rspeed(), PoliceCar.turn('right'))

# second var:

class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Новая машина: {self.name} цвет: {self.color} полиция? {self.is_police}')

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} поевернула {"налево" if direction == 0 else "нааправо"}')

    def speed(self):
        print(f'Машина {self.name} скорость {self.speed}')


class TownCar(Car):
    def speed(self):
        print(
            f'Машина {self.name} скорость {self.speed} {"Превышение скорости!" if self.speed > 60 else "Скорость нормальная"}')


class WorkCar(Car):
    def speed(self):
        print(
            f'Машина {self.name} скорость {self.speed} {"Превышение скорости!" if self.speed > 40 else "Скорость нормальная"}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town_car = TownCar('KIA', 'asphalt', 50)
town_car.turn(0)
town_car.speed()

work_car = WorkCar('Truck', 'blue', 70)
work_car.go()
work_car.speed()

police_car = PoliceCar('Police', 'white', 120)
police_car.stop()
police_car.speed()
print(police_car.is_police)


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение
# метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'"Запуск отрисовки"'


class Pen(Stationery):
    def draw(self):
        return f'"Запуск отрисовки":  {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'"Запуск отрисовки":  {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'"Запуск отрисовки":  {self.title}'


pen = Pen('Ручкой')
pencil = Pencil('Карандашом')
handle = Handle('Маркером')
print(pen.draw() + '\n' + pencil.draw() + '\n' + handle.draw())


