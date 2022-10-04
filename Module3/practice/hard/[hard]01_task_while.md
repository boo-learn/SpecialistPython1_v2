## "Число Фибоначчи"

### Задание

По данному числу n определите n-е [число Фибоначчи](https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8).

### Формат входных данных

Дано целое положительное число n, номер числа Фибоначчи в последовательности.

### Формат выходных данных

Вывести число Фибоначчи с номером n.


### Решение задачи

```python
n = int(input("n:"))
if n == 0:
    fibonacci_number = 0
elif n == 1:
    fibonacci_number = 1
elif n == 2:
    fibonacci_number = 1
else:
    previous_previous_number = 0
    previous_number = 1
    fibonacci_number = 1
    current_position = 3
    while current_position < n:
        fibonacci_number += previous_number
        previous_previous_number = previous_number
        previous_number = fibonacci_number - previous_previous_number
        current_position += 1
print(fibonacci_number)

```

### Данные для самопроверки

| Дано | Результат |
| :---: | --- |
|    1    | 0 |
|    4    | 2 |
|    7    | 8  |
|    11    | 55 |
