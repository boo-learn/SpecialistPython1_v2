def even(...):
    ...
    return ...

n = ...
if even(n):
   print("Число четное")
else:
   print("Число не четное")


def even(n):
    if n % 2 == 0:
        return True
    return False

n = int(input('Введите число: '))
if even(n):
   print("Число четное")
else:
   print("Число не четное")
