# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

tup1 = (18, 43, 56, 78, 89, 23, 11, 11)
tup2 = (35, 56, 78, 89, 22, 11, 11)
tup3 = (45, 56, 99, 78, 13, 19, 11, 11)

common_numbers = []

for i in tup1:
    for j in tup2:
        for k in tup3:
            if i == j == k and i not in common_numbers: # учитываем повтор только один раз
                common_numbers.append(i)

# print(common_numbers) # для проверки
print(len(common_numbers))
