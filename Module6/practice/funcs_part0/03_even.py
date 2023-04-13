def even(a):
    if a % 2 != 0:
        return False
    return True


n = int(input("Введите число: "))
if even(n):
    print("Число четное")
else:
    print("Число не четное")
