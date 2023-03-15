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
# TODO: you code here...
```
text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"

#Определить в предоставленном сообщении количество слов длиной больше, чем 5
arr = text.split(" ")
#print(arr[0])
i = 0
counter = 0
while i < len(arr):
    if len(arr[i]) >= 5:
        counter += 1
    i += 1
print(counter)
---

