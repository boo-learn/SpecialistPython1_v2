# Напишите функцию, возвращающую наибольшее из четырех чисел

def max4(n1, n2, n3, n4):
    # TODO: your code here
    nums = [n1, n2, n3, n4]
    maximum = nums[0]
    for n in nums:
        if n > maximum:
            maximum = n
    return maximum


# Тестируем функцию
print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 2.6, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -2, -2))
