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

find_circles = text.count(" ") + 1
start_pos = 0
end_pos = text.find(" ")
word_count = 0

while find_circles > 0:
    find_circles -= 1
    if len (text[start_pos:end_pos]) > 5:
        word_count += 1
    start_pos = end_pos + 1
    if text.find(" ", start_pos + 1) < 0:
        end_pos = len(text)
    else:
        end_pos = text.find(" ", start_pos + 1)

print(word_count)
```

---

