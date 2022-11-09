# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
text = "азаза уши уши тралала бабаба буба баскервиль"
first_letter = text.find(' б') + 1 if text[0] != 'б' else 0
if first_letter < 0:
    print("слов на б нет")
else:
    last_letter = text.find(" ", first_letter + 1) + 1 #срез не включает правую границу
    print(text[first_letter: last_letter if last_letter > 0 else len(text)])
