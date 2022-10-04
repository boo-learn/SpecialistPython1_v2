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
a = int(input("a:"))
b = int(input("b:"))
current_number = a
perfect_number_counter = 0
while current_number <= b:
    divider = 2
    dividers_sum = 1
    while divider <= current_number / 2:
        if current_number % divider == 0:
            dividers_sum += divider
        divider += 1
    if dividers_sum == current_number and current_number != 1:
        print("Число", current_number, "- совершенное!")
        perfect_number_counter += 1
    current_number += 1
print("Количество совершенных в интервале [", a, ", ", b, "]:", perfect_number_counter)

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
