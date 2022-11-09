# Даны примеры создания кортежей.
# Выясните, какие из них являются корректными.
# Все некорректные объявления и создающие не котрежи закомментируйте (#)
tup1 = (2, 4, -6)
tup2 = (2, "Василия", -6)
tup3 = 2, 4, -6
tup4 = (2)
tup5 = (2,)
tup6 = 2,
tup7 = tuple([2, 4, -6, 12])
# tup8 = tuple(2, 7, 8, -5)
tup9 = tuple()
tup10 = tuple("hello")
tup11 = ()
tup12 = 2 and 4

if tup1.__class__.__name__ == "tuple":
    print("Переменная tup1 является кортежем, её тип ", type(tup1))
else:
    print("Переменная tup1 не является кортежем, её тип ", type(tup1))
if tup2.__class__.__name__ == "tuple":
    print("Переменная tup2 является кортежем, её тип ", type(tup2))
else:
    print("Переменная tup2 не является кортежем, её тип ", type(tup2))
if tup3.__class__.__name__ == "tuple":
    print("Переменная tup3 является кортежем, её тип ", type(tup3))
else:
    print("Переменная tup3 не является кортежем, её тип ", type(tup3))
if tup4.__class__.__name__ == "tuple":
    print("Переменная tup4 является кортежем, её тип ", type(tup4))
else:
    print("Переменная tup4 не является кортежем, её тип ", type(tup4))
if tup5.__class__.__name__ == "tuple":
    print("Переменная tup5 является кортежем, её тип ", type(tup5))
else:
    print("Переменная tup5 не является кортежем, её тип ", type(tup5))
if tup6.__class__.__name__ == "tuple":
    print("Переменная tup6 является кортежем, её тип ", type(tup6))
else:
    print("Переменная tup6 не является кортежем, её тип ", type(tup6))
if tup7.__class__.__name__ == "tuple":
    print("Переменная tup7 является кортежем, её тип ", type(tup7))
else:
    print("Переменная tup7 не является кортежем, её тип ", type(tup7))
if tup9.__class__.__name__ == "tuple":
    print("Переменная tup9 является кортежем, её тип ", type(tup9))
else:
    print("Переменная tup9 не является кортежем, её тип ", type(tup9))
if tup10.__class__.__name__ == "tuple":
    print("Переменная tup10 является кортежем, её тип ", type(tup10))
else:
    print("Переменная tup10 не является кортежем, её тип ", type(tup10))
if tup11.__class__.__name__ == "tuple":
    print("Переменная tup11 является кортежем, её тип ", type(tup11))
else:
    print("Переменная tup11 не является кортежем, её тип ", type(tup11))
if tup12.__class__.__name__ == "tuple":
    print("Переменная tup12 является кортежем, её тип ", type(tup12))
else:
    print("Переменная tup12 не является кортежем, её тип ", type(tup12))
