import random

def average(*args):
    return sum(args) / len(args)


def gen_list(size, at=-10, to=10):
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(at, to))
    return result_list


my_list = gen_list(10)
my_tuple = 5, 7, -4, 10, 8

res = average(*my_list)
res1 = average(*my_tuple)

print(res)
print(res1)
