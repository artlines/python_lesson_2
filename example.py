# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
for i in range(1, 6):
    print(i, 0)
'''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
i, match_quantity = 0, 0

while i < 10:
    if int(input('Введите число ')) == 5:
        match_quantity += 1
    i += 1
print('Количество цифр 5: ', match_quantity)

'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1, 101):
    sum += i
print(sum)

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
op = 1

for i in range(1, 11):
    op *= i
print(op)

'''
Задача 5

Вывести цифры числа на каждой строчке.
'''
integer_number = 2129

while integer_number > 0:
    print(integer_number % 10)
    integer_number = integer_number // 10

'''
Задача 6

Найти сумму цифр числа.
'''
sum = 0
integer_number = 2129

while integer_number > 0:
    sum += integer_number
    integer_number = integer_number // 10
print(sum)

'''
Задача 7

Найти произведение цифр числа.
'''
op = 1
integer_number = 2129

while integer_number > 0:
    op *= integer_number
    integer_number = integer_number // 10
print(op)
'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
while integer_number > 0:
    if integer_number % 10 == 5:
        print('Yes')
        break
    integer_number = integer_number // 10
else:
    print('No')

'''
Задача 9

Найти максимальную цифру в числе
'''
max_number = 0
integer_number = 213413

while integer_number > 0:
    number = integer_number % 10
    print('number is', number)

    if number > max_number:
        max_number = number
    integer_number = integer_number // 10
print('max number is ', max_number)
'''
Задача 10

Найти количество цифр 5 в числе
'''

fives_quantity = 0
integer_number = 555

while integer_number > 0:
    number = integer_number % 10
    print('number is', number)

    if number == 5:
        fives_quantity += 1
    integer_number = integer_number // 10
print('fives quantity is ', fives_quantity)