## "Шахматы: слон"

### Задание

Требуется определить, бьет ли слон, стоящий на клетке с указанными координатами (номер строки и номер столбца), фигуру, стоящую на другой указанной клетке.

### Формат входных данных

Даны четыре числа целые числа в диапазоне [1, 8], координаты слона и координаты другой фигуры

### Формат выходных данных

Вывести "Да", если слон бьет фигуру или "Нет", если не бьет.

### Решение задачи

```python
print('Введи координаты слона')
x_el = int(input('x = '))
y_el = int(input('y = '))
print('Введи координаты фигуры')
x_fig = int(input('x = '))
y_fig = int(input('y = '))

if x_fig == x_el + 2 and y_fig == y_el + 1:
    print('бьет')
elif x_fig == x_el + 2 and y_fig == y_el - 1:
    print('бьет')
elif x_fig == x_el - 2 and y_fig == y_el + 1:
    print('бьет')
elif x_fig == x_el - 2 and y_fig == y_el - 1:
    print('бьет')
elif y_fig == y_el + 2 and x_fig == x_el + 1:
    print('бьет')
elif y_fig == y_el + 2 and x_fig == x_el - 1:
    print('бьет')
elif y_fig == y_el - 2 and x_fig == x_el + 1:
    print('бьет')
elif y_fig == y_el - 2 and x_fig == x_el - 1:
    print('бьет')
else:
    print('не бьет')
```

---
