## "Подсчет положительных"

n = int(input("n: "))
i = 0
num_positive = 0  # Счетчик положительных чисел
while i < n:
    number = int(input("number: "))
    print(number)  # то выводим его
    if number > 0 :  # Если число положительно
        num_positive = num_positive + 1
    i = i+1
print("Было введено", num_positive, "положительных чисел")

