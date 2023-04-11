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

LENGTH_LIMIT = 5
split_text = text.split(" ")

i = 0
count = 0

while i < len(split_text):
    if len(split_text[i]) > LENGTH_LIMIT:
        count += 1
    i += 1

print("Длинных слов -", count)
```

---

