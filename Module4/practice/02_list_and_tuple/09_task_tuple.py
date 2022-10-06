# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

a = (2, 3, 5, 'gg', 'wp')
b = (34, 23, 'gg', 'wp', 'ups')
c = ('gg', 'wp', 45)

counter = 0
for element in a:
    if (element in b) and (element in c):
        counter += 1
      
print(counter)
