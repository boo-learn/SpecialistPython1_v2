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
tup8 = tuple(2, 7, 8, -5)
tup9 = tuple()
tup10 = tuple("hello")
tup11 = ()
tup12 = 2 and 4


tup1 = (2, 4, -6)
tup2 = (2, "Василия", -6)
tup3 = 2, 4, -6
tup4 = (2)                    # int
tup5 = (2,)
tup6 = 2,
tup7 = tuple([2, 4, -6, 12])
# tup8 = tuple(2, 7, 8, -5)   # incorrect!
tup9 = tuple()
tup10 = tuple("hello")
tup11 = ()
tup12 = 2 and 4               #int

print("Type of tup1: ", type(tup1))
print("Type of tup2: ", type(tup2))
print("Type of tup3: ", type(tup3))
print("Type of tup4: ", type(tup4))
print("Type of tup5: ", type(tup5))
print("Type of tup6: ", type(tup6))
print("Type of tup7: ", type(tup7))
#print("Type of tup8: ", type(tup8))
print("Type of tup9: ", type(tup9))
print("Type of tup10: ", type(tup10))
print("Type of tup11: ", type(tup11))
print("Type of tup12: ", type(tup12))
