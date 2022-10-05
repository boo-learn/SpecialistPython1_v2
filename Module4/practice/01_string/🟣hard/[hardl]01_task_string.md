## "Подсчет длинных слов"

### Задание

Определить в предоставленном сообщении количество слов длиной больше, чем 5.

### Формат входных данных

Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.

### Формат выходных данных

Вывести количество найденных слов.

### Решение задачи

```python
s = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
i=0
tot=0
while i<len(s.split(" ")):
    if len(s.split(" ")[i])>5:
        tot+=1
    i+=1
print(tot)
```

---

