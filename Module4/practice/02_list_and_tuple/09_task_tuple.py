# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

elem_in_all_tuples = 0
for elem in tup1:
    if elem in tup2 and elem in tup3:
        elem_in_all_tuples += 1

print(elem_in_all_tuples)
