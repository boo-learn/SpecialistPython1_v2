def palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
