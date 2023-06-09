# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# Способ 1

# number = int(input("Введите трехзначное число: "))

# number_sum = number // 100 + number // 10 % 10 + number  % 10

# print(number_sum)

# Способ 2

# number = (input("Введите число: "))

# number_sum = 0

# for i in number:
#     number_sum += int(i)

# print(number_sum)

# Способ 3

# print(sum(map(int, input())))




# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:***9*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# 7 -> "Нельзя определить"


# number = int(input("Введите число сделанных журавликов: "))

# if number % 6 == 0:
#     pete = sergey = number // 6
#     kate = number // 6 * 4
#     print(pete, sergey, kate)
# else:
#     print("Нельзя определить")


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no
#     001001 -> yes

# number_ticket = int(input("Введите шестизначный номер билета: "))

# if number_ticket // 1000000 == 0:
#     nt1 = number_ticket // 100000 + number_ticket // 10000 % 10 + number_ticket // 1000 % 10
#     nt2 = number_ticket // 100 % 10 + number_ticket // 10 % 10 + number_ticket  % 10

#     if nt1 == nt2:
#         print("Счастливый билет")
#     else: 
#         print("Несчастливый билет")
# else: 
#         print("Введите шестизначный номер билета: ")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Укажите размер стороны n "))
m = int(input("Укажите размер стороны m "))
k = int(input("Укажите необходимое количество долек "))

if k < n*m and (k % n == 0 or k % m == 0):
    print("Вы можете отломить необходимое количество долек от шоколадки")
else:
    print("Вы не можете отломить от шоколадки данное количество долек")