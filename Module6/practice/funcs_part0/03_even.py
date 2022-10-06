def even(n):
    return n % 2 == 0


n = int(input("Enter number: "))
if even(n):
    print("Число четное")
else:
    print("Число не четное")
