# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here
tuple1 = 1,3,54,3,44,21,3
tuple2 = 9,3,1,6,34,7,3,2
tuple3 = 4,3,5,1,7,5,8,9

matches = []
for t1 in tuple1:
    for t2 in tuple2:
        for t3 in tuple3:
            if t1 == t2 == t3 and t1 not in matches:
                matches.append((t1))
print(matches)
