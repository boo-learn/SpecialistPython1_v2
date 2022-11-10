path = "numbers.txt"

f = open(path, "r")
sum_numbers = 0
count = 0
for line in f:
    count += 1
    sum_numbers += int(line)

average = sum_numbers / count

f.close()

print(f"Сумма чисел = {sum_numbers}")
print(f"Среднеарифметическое = {average}")
