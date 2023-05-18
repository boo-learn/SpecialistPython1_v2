# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу не используя строки

def palindrome(n: int) -> bool:
    digits = []
    digits_reverse = []
    mult = 1
    while abs(n) // mult > 0:
        digits.append(n % (mult * 10) // mult)
        mult *= 10
    digits_reverse = digits.copy()
    digits_reverse.reverse()
    i = 0
    for digit in digits:
        if digit != digits_reverse[i]:
            return False
        i += 1
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
