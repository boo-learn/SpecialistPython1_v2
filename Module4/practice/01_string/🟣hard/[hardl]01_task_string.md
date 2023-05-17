## "Подсчет длинных слов"

### Задание

Определить в предоставленном сообщении количество слов длиной больше, чем 5.

### Формат входных данных

Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.

### Формат выходных данных

Вывести количество найденных слов.

### Решение задачи

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"

count = 0
text_rest = text.strip().replace("  ", " ")
while text_rest.find(" ") != -1:
    word = text_rest[:text_rest.find(" ")]
    if len(word) > 5: count += 1
    text_rest = text_rest[text_rest.find(" ")+1:]

print("count: ", count)
