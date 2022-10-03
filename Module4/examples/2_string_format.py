# ================================
#       Форматирование строк
# ================================

name = 'Иван'
surname = 'Иванов'
# Плохой способ
print('Welcome, ' + surname + ' ' + name + ', to our conference')

# Старый способ форматирования
print('Welcome, %s %s, to our conference' % (name, surname))

# Более новый и гибкий метод
print('Welcome, {} {}, to our conference'.format(name, surname))
print('Welcome, {1} {0}, to our conference'.format(name, surname))

# Самый новый способ (работает с версии python 3.6)
print(f'Welcome, {name} {surname}, to our conference')  # f-строки наше все -)

# Подробнее в справочнике или документации
