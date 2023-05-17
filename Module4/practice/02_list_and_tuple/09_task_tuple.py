# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

tuple1 = (1, 2, 3, 4, 5 )
tuple2 = (1, 1, 3, 3, 5, 7, 8)
tuple3 = (2, 2, 4, 4, 5, 9, 9, 10)

numb_element = 0
for var in tuple1:
    if tuple2.count(var) > 0 and tuple3.count(var) > 0:
        numb_element += tuple1.count(var) + tuple2.count(var) + tuple3.count(var)

print(numb_element)
