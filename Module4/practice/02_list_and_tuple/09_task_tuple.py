# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

import random
n = 10
a = []
b = []
c = []
i = 0
while i < n:
    a.append(random.randint(1, 10))
    b.append(random.randint(1, 10))
    c.append(random.randint(1, 10))
    i += 1
a, b, c = tuple(a), tuple(b), tuple(c)
print('Кортеж 1: ', a)
print('Кортеж 2: ', b)
print('Кортеж 3: ', c)
print('Совпадения:', end=" ")
d=[]
for number in a:
    if b.count(number) != 0:
        if c.count(number) != 0:
            if d.count(number)==0:
                d.append(number)
                print(number, end=" ")
