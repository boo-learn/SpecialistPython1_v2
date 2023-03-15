# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here
tup1 = (10, 4, 6, -4, 12, 0, 5, 2)
tup2 = (2, 4, -6)
tup3 = (3, 4, 2)

min_element = min(tup1 + tup2 + tup3)
max_element = max(tup1 + tup2 + tup3)
# print(min_element)
# print(max_element)
counter = 0
while min_element < max_element:
    if min_element in tup1 and min_element in tup2 and min_element in tup3:
        counter +=1
    min_element += 1
print("Found same elements: ", counter)
