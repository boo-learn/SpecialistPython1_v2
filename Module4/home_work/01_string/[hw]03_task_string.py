# Посчитайте количество согласных букв в данной строке.

text = 'Отправлено уведомление о переводе служебной записки в статус "Завершена"'
constants = "бвгджзйклмнпрстфхцчшщ"
num_const = 0
for letter in text:
    if letter.isalpha():
        for const in constants:
            if letter == const:
                num_const += 1
                print(letter)
print(num_const)

