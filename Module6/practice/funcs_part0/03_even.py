def even(number: int):
    if number % 2 == 0:
        return True
    return False


n = 5
if even(n):
    print("Число четное")
else:
    print("Число не четное")
