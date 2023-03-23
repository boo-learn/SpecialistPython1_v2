# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
def num_elements_sum(number):
    number_string = str(number)
    summ = 0
    for num in number_string:
        summ += int(num)
    return summ


# print(num_elements_sum(123))
# print(num_elements_sum(10))
# print(num_elements_sum(9))
# print(num_elements_sum(8))
# print(num_elements_sum(321))

# print("#"*30)

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) == 6:
        first_part = ticket_number // 1000
        second_part = ticket_number % 1000
        # print(first_part)
        # print(second_part)
        return num_elements_sum(first_part) == num_elements_sum(second_part)
    else:
        return f"ERROR. Username, You tried '{ticket_number}' Please set correct ticket num."


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(486751))
print(lucky_ticket(1486751))
