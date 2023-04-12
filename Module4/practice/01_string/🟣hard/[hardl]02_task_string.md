## "Подсчет длинных слов"

### Задание

Даны две строки s1 и s2. Определите, можно ли составить строку s2, используя только символы из строки s1 (каждую букву можно использовать только один раз).

### Формат входных данных

Даны две строки.

### Формат выходных данных

Вывести "Да", если из символов строки s1 можно составить строку s2 и "Нет", если нельзя.

### Решение задачи

```python
# [hardl]02_task_string.md
# "Подсчет длинных слов"
# Даны две строки s1 и s2. Определите, можно ли составить строку s2, используя только символы из строки s1
# (каждую букву можно использовать только один раз).

#text = "Aorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
text = "orem ipsum dolor sit amet consectetur adipiscing elit nteger porttitor bibendum nisi ut convallis ante"
alphabet = "abcdefghijklmnopqrstuvwxyz "

i = 0
flag = True

while i < len(text):
    if not text[i] in alphabet:
        flag = False
    i += 1
if flag:
    print("Да")
else:
    print("Нет")
 
```

---

