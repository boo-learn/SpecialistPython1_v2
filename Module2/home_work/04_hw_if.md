## "Воздушные шарики"

k = int(input("Можно ли купить такое количество шаров?:"))
part_1 = 5
part_2 = 3

if k % part_1 == 0 or k % part_2 == 0 or k% (part_1+part_2) == 0:
    print("Yes")
else:
    print("No")
