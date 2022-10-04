## "FooBar"
number = int(input("Ввести целое число: "))

if number % 5 == 0 and number % 3 == 0:
    print("FooBar")
elif number % 3 == 0:
    print("Foo")
elif number % 5 == 0:
    print("Bar")

