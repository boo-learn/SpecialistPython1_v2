## "Числа по порядку"

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if c < b < a:
    a, b, c = c, b, a
elif b < c < a:
    a, b, c = b, c, a
elif b < a < c:
    a, b, c = b, a, c
elif a < b < c:
    a, b, c = a, b, c
elif a < c < b:
    a, b, c = a, c, b
print(a, b, c)
