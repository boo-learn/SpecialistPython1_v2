## "Дружественные числа"

### Задание

Два натуральных числа называются дружественными, если каждое из них равно сумме всех натуральных делителей другого
(само число при этом не рассматривается в качестве собственного делителя). \
Необходимо найти все пары натуральных дружественных чисел (не равных друг другу), до введенного числа.

### Формат входных данных

Дано одно целое положительное число

### Формат выходных данных

Вывести все пары дружественных чисел, удовлетворяющие условию задачи.

### Решение задачи

```python
end_number = int(input("n: "))
current_n = 1
i = 1
j = 1
while current_n <= end_number:  # перебираем все числа

    n_divider_sum = 0

    n_friend = 1

    while i <= current_n:  # вычисление суммы делителей числа current_n
        if (current_n % i == 0) and i != current_n:
            n_divider_sum += i
        i += 1

    while n_friend <= end_number:  # перебираем всех потенциальных "друзей"

        n_friend_divider_sum = 0
        while j <= n_friend:  # вычисление суммы делителей потенциального числа -"друга"
            if (n_friend % j == 0) and j != n_friend:
                n_friend_divider_sum += j
            j += 1
#
        if n_friend_divider_sum == current_n and n_divider_sum == n_friend and current_n != n_friend and current_n < n_friend :
            print(current_n, n_friend)
        n_friend += 1
        j = 1

    i = 1
    n_friend = 1
    current_n += 1

```

---

### Данные для самопроверки

| Дано | Результат |
| :---: | --- |
|  300  | 220 284 |
