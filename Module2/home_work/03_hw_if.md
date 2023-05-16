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
chess_pos_one = int(input("Chess_pos_one: "))
chess_pos_two = int(input("Chess_pos_two: "))
chess_pos_three = int(input("Chess_pos_three: "))
chess_pos_four = int(input("Chess_pos_four: "))

color_chess_one = (chess_pos_one + chess_pos_two) % 2
color_chess_two = (chess_pos_three + chess_pos_four) % 2

if color_chess_one == color_chess_two:
    print("Да")
else:
    print("Нет")

```

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
