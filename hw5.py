# 1. Создать программно файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода
# данных свидетельствует пустая строка.

f = open('5.1.txt', 'w')
line = input('Input: \n')
while line:
    f.writelines(line)
    line = input('Input: \n')
    if not line:
        break
f.close()

f = open('5.1.txt', 'r')
content = f.readlines()
print(content)
f.close()

#короткий варинат кода:
with open('5.1.txt', 'w', encoding='utf-8') as f:
    line = ' '
    while line != '':
        line = input()
        print(line, file=f)

# 2. Создать текстовый файл (не программно), сохранить в нем
# несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

str = open('5.2.txt', 'r')
content = str.readlines()
print(f'str: {len(content)}')
words = open('5.2.txt', 'r')
content = words.read()
content = content.split()
print(f'words: {len(content)}')
words.close()

#короткий варинат кода:
with open('5.2.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    for i, line in enumerate(text, 1):
        words = len(line.split())
        print(f'{i}ая строка содержит {words} слов')

# 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников
# имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('5.3.txt', 'r') as salary:
    sal = []
    avsal = []
    lst = salary.read().split('\n')
    for i in lst:
        i = i.split()
        if int(i[1]) < 20000:
           avsal.append(i[0])
        sal.append(i[1])
        avsalary = round(sum(map(int, sal)) / len(sal), 1)
print(f'Salary > 20.000 {avsal}\nAverage salary = {avsalary}')

# 2 вариант исполнения кода:
total_w = 0
empl = 0
with open('5.3.txt', 'r') as salary:
    for line in salary:
        total_w += float(line.split()[1])
        empl += 1
        if float(line.split()[1]) > 20000:
            print(line.split()[0])
print('Средняя величина дохода: ', round(total_w / empl, 2))

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

res = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
second = []
with open('5.4.txt', 'r', encoding='utf-8') as first:
    for i in first:
        i = i.split(' ', 1)
        second.append(res[i[0]] + '  ' + i[1])
with open('5.4.1.txt', 'w') as file_obj_2:
    file_obj_2.writelines(second)

# еще один вариант кода:
res = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('5.4.1.txt', 'w', encoding='utf-8') as f_write:
    with open('5.4.txt', 'r', encoding='utf-8') as f_read:
        for line in f_read:
            f_write.writelines([line.replace(line.split()[0], res[line.split()[0]])])


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.

def my_func():
    while True:
        try:
            with open('5.5.txt', 'w+') as file_obj:
                line = input('Input numbers separated by a space\n')
                file_obj.writelines(line)
                numb = line.split()
                print(sum(map(int, numb)))
        except ValueError:
            print('Error')
my_func()

# еще один вариант кода:
from random import randint

with open('5.5.txt', 'w', encoding='utf-8') as file_obj:
    li = [randint(1, 20) for _ in range(50)]
    file_obj.write(' '.join(map(str, li)))

print('Сумма чисел: ', sum(li))

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и
# лабораторных занятий по этому предмету и их количество. Важно,
# чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('5.6.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()
    for line in text:
        new = ''
        for el in line:
            new = ''.join([new, (el if el in '0123456789' else ' ')])
        res = [int(i) for i in new.split()]
        print(f'{line.split()[0]} - {sum(res)} часов')


# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки,
# в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать
# словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000},
# {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('5.7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('5.7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')

#короткий варинат кода:
import json

with open('5.7.json', 'w', encoding='utf-8') as f_write:
    with open('5.7.txt', 'r', encoding='utf-8') as f_read:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_read}
        res = [profit,{'average_profit': sum([int(i) for i in profit.values() if int(i) > 0]) /
                       len([int(i) for i in profit.values() if int(i) > 0])}]
    json.dump(res, f_write)
