## "Сумма четных чисел"

n = int(input("n: "))

i = 0
summa = 0
while i <= n:
    if i % 2 == 0:
        summa += i
    i += 1
print(summa)
