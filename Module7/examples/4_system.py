import sys

# Список аргументов запуска скрипта, первым аргументом является полный путь к файлу скрипта
print('sys.argv = ', sys.argv)
# Список путей для поиска модулей
print('sys.path = ', sys.path)
# Полный путь к интерпретатору
print('sys.executable = ', sys.executable)
# словарь имен загруженных модулей
print('sys.modules = ', sys.modules)
# Информация об операционной системе
print('sys.platform = ', sys.platform)

while True:
    key = input("press 'q' to Exit")

    if key == 'q':
        sys.exit()  # Вызов данной функции мгновенно завершает работу модуля (скрипта)
