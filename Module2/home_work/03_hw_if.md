## "Клетки шахматной доски"

### Задание

Имеем стандартное поле шахматной доски размеров 8x8

![board.png](img/board.png)

Даны координаты двух клеток на шахматной доске.

Определить, одинакового ли цвета клетки?

### Формат входных данных

Даны четыре целые числа в диапазоне [1, 8]

### Формат выходных данных

Вывести "Да", если клетки с заданными координатам одинакового цвета, и "Нет", если разного.

### Решение задачи

```python
# TODO: you code here...
```
# Chess
xa = int(input("Please set XA: "))
ya = int(input("Please set YA: "))
xb = int(input("Please set XB: "))
yb = int(input("Please set YB: "))

if (xa % 2) + (ya % 2) != 0:
    a_colour = "black"
else:
    a_colour = "white"

if (xb % 2) + (yb % 2) != 0:
    b_colour = "black"
else:
    b_colour = "white"

print("a_colour is:", a_colour)
print("b_colour is:", b_colour)
if a_colour == b_colour:
    print("Same Colours")
else:
    print("Different Colours")

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Условие для проверки четности числа:

```python
n % 2 == 0
```

</details>

<details>
<summary>Подсказка-2</summary>
Сумма двух нечетных чисел, всегда четная.
</details>
