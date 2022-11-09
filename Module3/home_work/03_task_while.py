n = int(input("n: "))
i = 1
j = 1
while i <= n:
    while j <= n:
        print(str(i * j).rjust(2, " "), end = " ")
        j += 1
    j = 1
    i += 1
    print()
