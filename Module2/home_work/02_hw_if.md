## "Коровы"

### Задание

![board.png](img/cow2.gif) 

По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
 «n коров», «n корова», «n коровы», правильно склоняя слово «корова».

**Например**: 1 коров**а**, 2 коров**ы**, 5 коров, 125 коров, 414 коров, 424 коров**ы**.

### Формат входных данных

Дано целое положительное число n - количество коров

### Формат выходных данных

Программа должна вывести правильное(согласованное) окончание слова "корова": 
_коров_, _корова_ или _коровы_, для заданного числа n.

### Решение задачи

```python
# TODO: you code here...
```
# Cows
# 1 корова ; 2, 3, 4 коровы ; 5 коров
cows_value = int(input("Please set Cows number: "))

one_last = cows_value % 10
two_last = cows_value % 100
print("One Last digit is:", one_last)
print("Two Last digits is:", two_last)

letter = "На лугу пасется..."
letter += str(cows_value)+" "
word = "коров"
word_end = "Ы"

if two_last == 1 or (two_last > 20 and one_last == 1):
    word_end = "А"
elif two_last % 10 == 0 or one_last >= 5:
    word_end = "_"
elif two_last > 10 and two_last < 20:
    word_end = "__"
print(letter, word+word_end)

---
### Подсказки

<details>
<summary>Подсказка-1</summary>
Возьмите листок бумаги и выписывайте все согласования: <br>
<i>1 корова</i> <br>
<i>2, 3, 4 коровы</i> <br>
<i>5 коров</i><br>
... <br>
пока не найдете закономерность.
</details>
