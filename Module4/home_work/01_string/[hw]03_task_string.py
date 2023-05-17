# Посчитайте количество согласных букв в данной строке.

text = input('text: ')
vowels = ['а', 'о', 'и', 'ы', 'у', 'э', 'я', 'е']
letter_count = 0
count = len(text)
for letter in text:
    if letter in vowels:
        letter_count += 1
print(count - letter_count)
