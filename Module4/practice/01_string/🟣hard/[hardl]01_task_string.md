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
list1 = text.split(" ")
i = 0
Count = 0
while 0 <= i < len(list1):
    if len(list1[i]) > 5:
        Count += 1
    i += 1
print("число слов длиной больше 5:", Count)
```

---

