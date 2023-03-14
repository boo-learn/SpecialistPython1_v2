## "Шоколадка"

### Задание

![board.png](img/chocolat_lines.png)

Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек , если разрешается сделать один разлом
по прямой между дольками (то есть разломить шоколадку на два прямоугольника)

### Формат входных данных

Вводятся 3 целых положительных числа n, m и k. Точно известно, что k ≠ n ⋅ m.

### Формат выходных данных

Выведите "Да", если можно отломить от шоколадки ровно k долек, и "Нет" если нельзя.

### Решение задачи

```python
# TODO: you code here...
```
# Chocolate
n_size = int(input("Please set n: "))
m_size = int(input("Please set m: "))
k_value = int(input("Please set k value: "))
#if k_value == n_size * m_size or k_value > n_size * m_size:
#    print("You set incorrect values")
#elif k_value % n_size == 0 or k_value % m_size == 0:
#    print("You are correct")
#else:
#   print("Incorrect, please set correct values.")
if (k_value % n_size == 0 or k_value % m_size == 0) and k_value < (n_size * m_size):
    print("You set Correct values")
else:
    print("Incorrect, please set correct values.")

---

