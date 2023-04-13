# Используя функцию average() из предыдущей задачи, найдите среднее арифметическое всех элементов списка и кортежа

def average(*args):
    if not args:
        return None
    return sum(args) / len(args)
    pass


def gen_list(size, at=-10, to=10):
    import random
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(at, to))
    return result_list


my_list = gen_list(10)
my_tuple = 5, 7, -4, 10, 8

avg_list = average(*my_list)
avg_tuple = average(*my_tuple)

print(f"Среднее арифметическое списка {my_list}: {avg_list}")
print(f"Среднее арифметическое кортежа {my_tuple}: {avg_tuple}")
