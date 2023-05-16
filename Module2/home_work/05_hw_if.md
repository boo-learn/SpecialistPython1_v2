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
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# TODO: you code here...

if  a < b and b < c:
    t = 0
elif a > b and b < c and a < c:
    a, b = b, a
   
elif a > b and b < c and a > c:
    a, b = b, a
    c, b = b, c
   
elif a < b and b > c and a < c:
    c, b = b, c
   
elif a < b and b > c and a > c:
    a, b = b, a
    a, c = c, a
   
elif a > b and b > c: 
    a, c = c, a
   
else:
    u = 0
   
    
print(a, b, c)


print(a, b, c)
```

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Вспомните про задачу "поменять значения переменных местами".
</details>
