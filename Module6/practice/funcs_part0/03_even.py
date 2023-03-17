def even(n):
    if n%2 == 0:
        return True
    return False

n = int(input("n:"))
if even(n):
   print("Число четное")
else:
   print("Число не четное")
