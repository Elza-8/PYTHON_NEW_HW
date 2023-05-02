# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке
# натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

len_nums = int(input('Enter list length: '))
nums = [randint(1, 100) for i in range(len_nums)]
print("List: ", *nums)
x = int(input('Enter x: '))

min_diff = nums[0]
for i in nums:
    diff_current = abs(i-x)
    if diff_current < min_diff:
        min_diff = diff_current

res = min([i for i in nums if abs(i-x) == min_diff])
print(f'Result is {res}')

# print(f'Result is {min(nums, key=lambda y: abs(y-x))}')
