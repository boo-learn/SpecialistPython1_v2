def even(a):
    if a % 2 == 0:
        res = True
    else:
        res = False

    return res


n = 6
if even(n):
    print("Число четное")
else:
    print("Число не четное")
