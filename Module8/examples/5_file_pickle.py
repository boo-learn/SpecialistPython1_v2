import os
import pickle

DIR = 'files'
python_data = [{"name": 'Петр', 'age': 10}, {"name": 'Александр', 'age': 8}]

# Записываем объект Python в файл в виде бинарника
with open(os.path.join(DIR, 'save_pickle_data'), 'wb') as f:
    pickle.dump(python_data, f)

# Читаем данные их файла и преобразуем к типу Python (восстанавливаем объект из файла)
with open(os.path.join(DIR, 'save_pickle_data'), 'rb') as f:
    read_data = pickle.load(f)

print(read_data)
print(read_data[0])

# При помощи модуля pickle можно сохранять любые python-объекты
