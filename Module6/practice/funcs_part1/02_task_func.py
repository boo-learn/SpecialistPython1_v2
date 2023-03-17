# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу не используя строки

def palindrome(number):
    string_number = str(number)
    result = 0
    i = 0
    for num in string_number:
        i += 1
        if num == string_number[-i]:
            result += 1
        else:
            return False
    return True

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
