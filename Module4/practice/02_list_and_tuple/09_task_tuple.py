# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

tup1 = (2, 4, 6, -4, 12, 0, 5)
tup2 = (2, 4, 6, 50, 7, 9, 1, 11, 6)
tup3 = (5, 1, 2, 6)
match_counter = 0
for elem in tup1:
    match_counter += min(tup1.count(elem), tup2.count(elem), tup3.count(elem))
print(match_counter)
