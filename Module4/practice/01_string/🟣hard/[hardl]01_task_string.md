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
split_text = text.split()
print(split_text)
count = len(split_text)
i = 0
print(count)
result = 0
while i < count:
    if len(split_text[i]) > 5:
        result += 1
    i += 1
print(result)
# TODO: you code here...
```

---

