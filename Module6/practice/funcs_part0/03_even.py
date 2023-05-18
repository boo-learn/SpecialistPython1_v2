def even(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


n = int(input("number: "))
if even(n):
    print("Число четное")
else:
    print("Число не четное")
