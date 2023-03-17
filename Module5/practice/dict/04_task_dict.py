# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
high_salary = float(staff[2]['salary'])
for item in staff:
    if float(item['salary']) > high_salary:
        high_salary = float(item['salary'])
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")

low_salary = float(staff[2]['salary'])
for item_1 in staff:
    if float(item_1['salary']) < low_salary:
        low_salary = float(item_1['salary'])


print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

# TODO: your code here

print("Среднеарифметическую зарплату всех сотрудников")

# TODO: your code here

print("Количество однофамильцев в организации")

# TODO: your code here

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

# TODO: your code here
