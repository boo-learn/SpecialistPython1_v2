## "Число Фибоначчи"

### Задание

По данному числу n определите n-е [число Фибоначчи](https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8).

### Формат входных данных

Дано целое положительное число n, номер числа Фибоначчи в последовательности.

### Формат выходных данных

Вывести число Фибоначчи с номером n.


### Решение задачи

```python
# TODO: you code here...
```
# Число Фибоначчи
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,

position = int(input("Set position: "))
pre_previous = 0
previous = 1
next_one = 0
i = 3
if position == 1:
    print(pre_previous)
elif position == 2:
    print(previous)
else:
    while i <= position:
        next_one = pre_previous + previous
        pre_previous = previous
        previous = next_one
        i += 1
    # print(pre_previous)
    # print(previous)
    print(next_one)

### Данные для самопроверки

| Дано | Результат |
| :---: | --- |
|    1    | 0 |
|    4    | 2 |
|    7    | 8  |
|    11    | 55 |
