# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу не используя строки

def palindrome(number):
    number = str(number)
    half_len = int(len(number) / 2)
    if half_len % 2 == 0:
        if number[:half_len] == number[::-1][:half_len]:
            return "Да"
        else:
            return "Нет"
    else:
        if number[:half_len + 1] == number[::-1][:half_len + 1]:
            return "Да"
        else:
            return "Нет"


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))

# Подсказка:
# Самый простой способ решить задачу, работать с полученным числом как со строкой
# Преобразование к строке:  str(1234) --> "1234"
# Переворот строки:         "1234"[::-1] --> "4321"
