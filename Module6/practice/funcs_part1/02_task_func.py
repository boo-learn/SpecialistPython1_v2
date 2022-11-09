# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу не используя строки

def palindrome(number):
    func_in = number
    result = 0
    while number > 0:
        num = number % 10
        result = result * 10 + num
        number = number // 10
    if func_in == result:
        return f"Число {func_in} палиндром"
    else:
        return f"Число {func_in} не палиндром"


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
