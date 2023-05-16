## "Числа по порядку"

### Задание

Дано три целые числа. 

Упорядочите их в порядке возрастания.

![up](img/up.png)

### Формат входных данных

Даны три целые числа.

### Формат выходных данных

Вывести все числа от меньшего к большему.

#### Примечание

Предоставленную заготовку не менять. Ваша задача, написать алгоритм, который распределит значения трех переменных так, что в "a" будет наименьшее значение, а в "c" наибольшее.

### Решение задачи

```python
first_num = int(input("First_num: "))
second_num = int(input("Second_num: "))
third_num = int(input("Third_num: "))

if first_num > second_num:
    first_num, second_num = second_num, first_num
if second_num > third_num:
    second_num, third_num = third_num, second_num
if first_num > third_num:
    first_num, third_num = third_num, first_num
if first_num > second_num:
    first_num, second_num = second_num, first_num

print(first_num, second_num, third_num)
```

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Вспомните про задачу "поменять значения переменных местами".
</details>
