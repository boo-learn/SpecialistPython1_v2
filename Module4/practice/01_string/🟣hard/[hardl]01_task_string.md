## "Подсчет длинных слов"

### Задание

Определить в предоставленном сообщении количество слов длиной больше, чем 5.

### Формат входных данных

Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.

### Формат выходных данных

Вывести количество найденных слов.

### Решение задачи

```python
text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
i = 0
n = len(text)
n_simbol = 0
summa = 0

while i < n:
    if text[i] != " ":
        n_simbol += 1
    else:
        n_simbol = 0
    if n_simbol == 6:
        summa += 1
    i += 1

print("Количество слов больше 5 символов: ", summa)
```

---

