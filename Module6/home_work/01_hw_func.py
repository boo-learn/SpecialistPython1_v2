# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
import math

def lucky_ticket(tick_num):
    arr1 = [(tick_num//(10**i))%10 for i in range(math.ceil(math.log(tick_num, 10))-1, -1, -1)]
    if arr1[0]+arr1[1]+arr1[2] == arr1[3]+arr1[4]+arr1[5]:
        print("Билет счастливый!")
    else:
        print("Билет несчастливый(((")

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(123211))
print(lucky_ticket(436751))
