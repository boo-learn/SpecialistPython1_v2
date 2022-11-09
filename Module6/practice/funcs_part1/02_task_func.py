# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу не используя строки

def palindrome(number):
    pass


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))

# Solution
def palindrome(number):
    isPalindrom = False
    str_number = str(number)
    mediana = len(str_number) // 2
    if len(str_number) % 2 != 0:
        mediana += 1
    part1 = []
    part2 = []
    for index, digit in enumerate(str_number, 0):
        if index + 1 <= mediana:
            part1.append(digit)
        else:
            part2.append(digit)
    index = 0

    while index < len(part2) and part1[index] == part2[-(index+1)]:
        index += 1
    if index == len(part2):
        isPalindrom = True
    return isPalindrom


# Тестируем функцию
print(palindrome(34254))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
#

# Подсказка:
# Самый простой способ решить задачу, работать с полученным числом как со строкой
# Преобразование к строке:  str(1234) --> "1234"
# Переворот строки:         "1234"[::-1] --> "4321"
