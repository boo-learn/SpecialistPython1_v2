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
word_len = 0
num_long_words = 0

while i < len(text):
    if text[i] != " ":
        word_len += 1
    else:
        if word_len > 5:
            num_long_words += 1
        word_len = 0
    i += 1
if word_len > 5:
    num_long_words += 1

print(num_long_words)

```

---

