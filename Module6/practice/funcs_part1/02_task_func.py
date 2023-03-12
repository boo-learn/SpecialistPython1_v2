# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу не используя строки

def palindrome(number):
    if number < 0:  # отрицательные числа не могут быть палиндромами
        return False

    if number < 10:  # однозначные числа всегда палиндромы
        return True

    reversed_number = 0
    original_number = number

    while original_number > 0:
        digit = original_number % 10
        reversed_number = reversed_number * 10 + digit
        original_number //= 10

    return number == reversed_number
    pass


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
