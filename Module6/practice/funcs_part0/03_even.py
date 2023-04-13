def even(n):
    # Проверяем, делится ли число на 2 без остатка
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Введите целое число: "))

if even(n):
    print("Число четное")
else:
    print("Число не четное")
