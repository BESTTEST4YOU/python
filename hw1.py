#1. Work with variables, create a few, display,
# prompt the user for some numbers and strings and store them in variables,
# display.

a = int(input('Input number №1: '))
b = int(input('Input number №2: '))
t = str(input('Input symbols: '))
print('Output: ', a, b, t)

#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

n = int(input('Введите количество секунд: '))
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)
print(convert(n))

#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = (input("Введите число: "))
q = (n+n)
w = (n+n+n)
print(int(w) + int(q) + int(n))

#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

i = int(input('Введите число: '))
r = -1
while i > 10:
    d = i % 10
    i //= 10
    if d > r:
        r = d
print(r)

#5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

spend = int(input("Затраты: "))
v = int(input("Выручка: "))
workers = int(input("Штат: "))
profit = int(v - spend)
r = round(profit/v) #рентабельность
t = int(round(profit/workers)) #прибыль на 1 сотрудника
if profit > 0:
    print('Ваша фирма работает с прибылью: ', profit, 'руб.')
    print('Рентабельность выручки: ', r, '%')
    print('Прибыль фирмы в расчете на одного сотрудника: ', t, 'руб.')
else:
    print("Ваша фирма работает в убыток")