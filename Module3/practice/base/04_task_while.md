## "Подсчет положительных"

### Задание

Вводится n целых чисел. \
Посчитайте количество положительных чисел, среди введенных.

### Формат входных данных

Сначала вводится целое положительное n. \
Далее вводится n целых чисел.

### Формат выходных данных

Вывести количество положительных.

### Решение задачи

```python
# TODO: you code here...
```
n = int(input("insert n: "))
total = 0
num_positive = 0
while total < n:
    nx = int(input("insert nx: "))
    n = n - 1
    if nx > 0:
        num_positive = num_positive + 1
else:
    print()
print(num_positive)
---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Смотри пример "Нахождение количества чисел кратных трем в диапазоне [a, b]"
</details>

<details>
<summary>Подсказка-2</summary>
Воспользуйтесь заготовкой кода, дописав недостающие строки:

```python
n = int(input("n: "))
i = 0
num_positive = 0  # Счетчик положительных чисел
while i < n:
    number = int(input("number: "))
    ...
    ...
    # TODO: you code here...
    i += 1
print("Было введено", num_positive, "положительных чисел")
```
</details>

