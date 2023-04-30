# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые
# – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите
# минимальное количество монет, которые нужно перевернуть.
# Стороны монеты вводятся построчно или в одну строку, если умеете.

# Пример
# Ввод: 1 1 0 0 0 -> Вывод: 2

number_coins = int(input("Введите количество монет: "))
number_tails = 0

for i in range(number_coins):
    if input("Сторона монетки: ") == "0":
        number_tails += 1

if number_tails > number_coins - number_tails:
    print(number_coins - number_tails)
else:
    print(number_tails)