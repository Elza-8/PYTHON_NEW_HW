# Задача 36:
# На вход программы поступает строка в формате:

# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N

# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:

# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ...,
# ('ключ_N', 'значение_N'))

# Выводить на экран ничего не нужно, только преобразовать строку
# в кортеж с именем tp.

# Sample Input:

# house=дом car=машина men=человек tree=дерево
# Sample Output:
# (('house', 'дом'), ('car','машина'), ('men', 'человек'), ('tree', 'дерево'))


def zip_tuple(info: str) -> tuple[tuple]:
    """
    Принимает на вход строку вида:
    ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
    и преобразует ее в кортеж из пар
    (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ...,
    ('ключ_N', 'значение_N'))
    """
    return tuple(map(lambda x: tuple(x.split("=")), info.split()))


print(zip_tuple("house=дом car=машина men=человек tree=дерево"))