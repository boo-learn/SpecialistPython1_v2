## "Диагонали символами"

### Задание

Даны сторона квадрата. Вывести его диагонали символами #

### Формат входных данных

Дано целое число n, длина стороны квадрата. 1 < n < 20 

### Формат выходных данных

Вывести диагонали квадрата символами # (см. примеры)

#### Примеры

n = 6 
```
#    #
 #  #
  ##
  ##
 #  #
#    #
```
n = 3
```
# #
 #
# #
```
### Решение задачи

```python
# TODO: you code here...
n = int(input("n: "))

row_index = 0
while row_index < n:
    line = ""
    cell_index = 0
    while cell_index < n:
        if (cell_index == row_index) or (cell_index == (n - row_index - 1)):
            line += "#"
        else:
            line += " "
        cell_index += 1
    print(line)
    row_index += 1
```
