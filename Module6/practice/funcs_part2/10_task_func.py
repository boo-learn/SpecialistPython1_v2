# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов

def average(*args):
    # TODO: your code here
  def average(*args):
    # TODO: your code here
    summa = 0
    j = 0
    numbers = [*args]
    for i in numbers:
        summa = i + summa
        j += 1
    return summa / j


print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
