while True:
    data = input("Введите пять чисел: ")
    digits = data.split()
    try:
        if len(digits) != 5:
            raise ValueError
        
        min_value = int(digits[0])
        for digit in digits:
            if int(digit) < min_value:
                min_value = int(digit)
        break
    except ValueError:
        print("Некорректные параметры")

print(f"Минимальное значение : {min_value}")
