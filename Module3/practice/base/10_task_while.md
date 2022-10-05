## "Все совершенные число в диапазоне"

### Задание

Число совершенно, если оно равно сумме всех своих делителей, кроме самого себя. Пример: 6 = 1 + 2 + 3. \
Найдите все совершенные числа и их количество в заданном диапазоне [a, b].

### Формат входных данных

Даны два целых положительных числа, границы диапазона. Гарантируется, что a < b.

### Формат выходных данных

Вывести все совершенные числа, а затем их количество.

### Решение задачи

```python
a = int(input("a: "))
b = int(input("b: "))

number_of_perfect_numbers = 0
if a == 1:
    current_number = 2
else:
    current_number = a
while current_number <= b:
    denominator = 2
    sum_of_denominators = 1
    while denominator < int(current_number / 2) + 1:
        if current_number % denominator == 0:
            sum_of_denominators += denominator
        denominator += 1
    if sum_of_denominators == current_number:
        print(current_number)
        number_of_perfect_numbers += 1
    current_number += 1
print(f"Кол-во совершенных чисел = {number_of_perfect_numbers}")
```

---

### Подсказки
<details>
<summary>Подсказка-1</summary>
Для решения задачи вам понадобятся вложенные циклы.

```python
while ...:  # внешний цикл
    while ...:  # внутренний цикл
        ...
```
Внешний цикл будет перебирать числа из диапазона, а внутренний проверять, является ли число совершенным.
</details>

<details>
<summary>Подсказка-2</summary>
Для проверки числа на совершенность, воспользуйтесь решение предыдущей задачи "Совершенное число".
</details>
