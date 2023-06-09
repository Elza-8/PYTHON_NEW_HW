# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую
# сумму двух целых неотрицательных чисел. Из всех арифметических
# операций допускаются только +1 и -1. Также нельзя использовать циклы.
# return sum(a,b-1) + 1 - Так делать нельзя

# *Пример:*

# 2 2
#     4

def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    return sum(a + 1, b - 1)


first = int(input('Введите число A: '))
second = int(input('Введите число B: '))

result = sum(first, second)
print(f"Сумма чисел {first} и {second} равна {result}")
