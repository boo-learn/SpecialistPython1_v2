fruits = ["яблоко", "банан", "киви", "арбуз"]
max_len = len(max(fruits))

for i, fruit in enumerate(fruits, 1):
    if len(fruit)==max_len:
        print(i, ". ", fruit)
    else:
        n = max_len - len(fruit)
        print(i, ".", " " * n, fruit )
