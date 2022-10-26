# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
check_string = "Дана строка состоящая из слов начинающееся на букву б"

find_b=check_string.find("б")

if find_b>0:
    nachalo_slova=find_b
    konec_slova=nachalo_slova+check_string[find_b:].find(" ")
    print(nachalo_slova)
    print(konec_slova)
    print(check_string[nachalo_slova:konec_slova+1])
else:
    print("Нет слова на букву б")
