# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(lucky_ticket):
    lucky_ticket = str(lucky_ticket)
    if len(str(lucky_ticket)) == 6 and str(lucky_ticket[:3]) == str(lucky_ticket[:-4:-1]):
        return True
    else:
        return False

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436551))
print(lucky_ticket(436634))
print(lucky_ticket(4366348))
