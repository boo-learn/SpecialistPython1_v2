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
# TODO: you code here...
```
limit = 3000
number = limit
checked = []
while number > 0:
    if number not in checked:
        i = 1
        summ_number = 0
        while i < number:
            if number % i == 0:
                summ_number += i
            i += 1
        if summ_number > 0:
            j = 1
            check_summ_number = 0
            while j < summ_number:
                if summ_number % j == 0:
                    check_summ_number += j
                j += 1
            if check_summ_number > 0 and check_summ_number == number and summ_number != check_summ_number:
                print(number, summ_number)
                checked.append(summ_number)
            #print(number, summ_number)
        #checked.append(number)
    number -= 1
#print(checked)

---

### Данные для самопроверки

| Дано | Результат |
| :---: | --- |
|  300  | 220 284 |
