import sys
data_list = []
need_elements = 5
num_element = 1

while len(data_list) < need_elements:
    try:
        el = int(input(f"Введите целое число {num_element} из {need_elements}: "))
        data_list.append(el)
        num_element += 1
    except ValueError:
        print("Введены некоррекные данные, попробуйте снова")
    except EOFError:
        # Чтобы сработало это исключение, нажмите Ctrl+D
        print("Зачем же так грубо? -)")
        sys.exit()

print(data_list)
