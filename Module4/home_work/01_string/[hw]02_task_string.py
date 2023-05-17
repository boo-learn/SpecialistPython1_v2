# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
line = input("Введите строку: ")
first_letter_in_word = "б"
number = 0

for word in line.split():
    if word[0] == first_letter_in_word and number == 0:
        print(word)
        number += 1
if number == 0:
    print(f"слов на {first_letter_in_word} нет")
