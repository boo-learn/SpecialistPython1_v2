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
i=0
long_word_sign=5
word_length=0
long_words_num=0;
while i<len(text):
    if text[i]!=' ':
        word_length+=1
    else:
        if word_length>long_word_sign:
            long_words_num+=1
        word_length=0
    i+=1
    
print(long_words_num)
```

---

