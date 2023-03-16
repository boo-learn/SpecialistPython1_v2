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

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
text.lower() #перевел в нижний регистр. Видимо лишнее
text = text.split(' ') # разбили по пробелам

words = 0 # накопитель

for n in text:
    if len(n) > 5:
        words += 1 #подсчет при выполнении условия
print('Длина > 5:', words)


---

