def my_abs(a):
    if int(a) < 0:
        b = a * -1
        return b
    else:
        return a


print(my_abs(-5))
print(my_abs(5))
print(my_abs(0))
