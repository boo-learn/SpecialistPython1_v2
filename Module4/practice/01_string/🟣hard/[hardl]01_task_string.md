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
longstr_counter = 0
while i <= len(text) - 1:
    if text.find(" ") != -1:
        curr_word = text[:text.find(" ")]
        text = text[text.find(" ") + 1:]
        if len(curr_word) > 5:
            longstr_counter += 1
        print(curr_word)
        print(text)
        i += 1
print(longstr_counter)

```

---

