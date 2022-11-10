# Посчитайте количество согласных букв в данной строке.

string = "ДЕД с дробовиком"
the_number_of_consonant_letters_in_this_string = 0
for ind in ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']:
    the_number_of_consonant_letters_in_this_string += string.count(ind) + string.count(ind.lower())
if the_number_of_consonant_letters_in_this_string > 0:
    print("количество соласных букв в этой строке =", the_number_of_consonant_letters_in_this_string)
else:
    print("нет согласных")
