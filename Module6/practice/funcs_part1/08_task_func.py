# Напишите функцию находящую n-ое число Фибоначчи.

def fibonachi_num(n: int) -> int:
    first = 0
    second = 1
    count = 2
    result = 0
    if abs(n) == 1:
        return first
    elif abs(n) == 2:
        return second
    else:
        while count < abs(n):
            if n > 0:
                result = first + second
                first = second
                second = result
            else:
                result = first - second
                first = second
                second = result
            count += 1
        return result


n = int(input("n: "))
print(f"fibonachi_num {fibonachi_num(n)}")
