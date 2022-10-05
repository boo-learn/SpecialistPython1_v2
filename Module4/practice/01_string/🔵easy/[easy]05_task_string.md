## "Какая длиннее"

string1 = input("Первая строка:")
string2 = input("Вторая строка:")

if len(string1) > len(string2):
    print(string1)
elif len(string2) > len(string1):
    print(string2)
else:
    print(string1 or string2)
