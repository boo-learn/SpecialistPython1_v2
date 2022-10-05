# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
text = "У Быка бела куба была тупа."
count_w = 0
latter = ""
word = ""
for latter in text:
    if latter != " ":
        word += latter
    else:
        if word[0].lower() == "б":
            count_w += 1
            print(word)
        word = ""
if count_w == 0:
    print("слов на б нет")
else:
    print(count_w)
