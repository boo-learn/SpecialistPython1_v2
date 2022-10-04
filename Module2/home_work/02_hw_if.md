## "Коровы"

number = int(input("Ввести количество коров на лугу: "))

if number == 1:
    print("На лугу пасется", number, "коровa.")
elif number // 10 == 0 and number % 10 == 1:
    print("На лугу пасется", number, "коров.")
elif number // 10 == 1 and number % 10 == 2:
    print("На лугу пасется", number, "коров.")
elif number // 10 == 1 and number % 10 == 3:
    print("На лугу пасется", number, "коров.")
elif number // 10 == 1 and number % 10 == 4:
    print("На лугу пасется", number, "коров.")
elif number%10 == 2:
    print("На лугу пасется", number, "коровы.")
elif number%10 == 3:
    print("На лугу пасется", number, "коровы.")
elif number%10 == 4:
    print("На лугу пасется", number, "коровы.")
elif number%10 == 5:
    print("На лугу пасется", number, "коров.")
elif number % 10 == 1:
    print("На лугу пасется", number, "корова.")
else:
    print("На лугу пасется", number, "коров.")
