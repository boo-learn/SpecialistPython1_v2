a = int(input("a: "))
b = int(input("b: "))

if a > b:
    a, b = b, a
i = a
while i <= b:
    if i % 5 == 0:
        print(i)
    i += 1
