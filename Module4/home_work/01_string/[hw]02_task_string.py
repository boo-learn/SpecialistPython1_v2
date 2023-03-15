# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
text = "мама босс раму мыла балкон"
test = text.split(" ")
print(test)
check = False

for word in test:
    if word.startswith("б"):
        print(word)
        check = True
        break
if check == False:
    print("слов на Б нету")
