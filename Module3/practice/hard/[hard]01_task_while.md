## "Число Фибоначчи"

### Задание

По данному числу n определите n-е [число Фибоначчи](https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8).

### Формат входных данных

Дано целое положительное число n, номер числа Фибоначчи в последовательности.

### Формат выходных данных

Вывести число Фибоначчи с номером n.


### Решение задачи

n = int(input("n: "))

first = 0
second = 1
count = 2
result = 0

if abs(n) == 1:
    print(first)
elif abs(n) == 2:
    print(second)
elif n != 0:
    while count < abs(n):
        if n > 0:
            result = first + second
            first = second
            second = result
        else:
            result = first - second
            first = second
            second = result
        count += 1
    print(result)

### Данные для самопроверки

| Дано | Результат |
| :---: | --- |
|    1    | 0 |
|    4    | 2 |
|    7    | 8  |
|    11    | 55 |
