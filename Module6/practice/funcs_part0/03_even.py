def even(a):
    if a%2 == 0:
        c = True
    else:
        c = False
    return c

n = int(input("Ввести число:"))
if even(n):
   print("Число четное")
else:
   print("Число не четное")
