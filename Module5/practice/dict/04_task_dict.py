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

# Имя и Фамилию сотрудника с самой высокой зарплатой:
max_salary_employee = max(staff, key=lambda e: e['salary'])
print(f"{max_salary_employee['name']} {max_salary_employee['surname']}")

# Имя и Фамилию сотрудника с самой низкой зарплатой:
min_salary_employee = min(staff, key=lambda e: e['salary'])
print(f"{min_salary_employee['name']} {min_salary_employee['surname']}")

# Среднеарифметическую зарплату всех сотрудников
average_salary = sum(e['salary'] for e in staff) / len(staff)
print(f"{average_salary:.2f}")

# Количество однофамильцев в организации
surname_counts = {}
for employee in staff:
    surname = employee['surname']
    if surname in surname_counts:
        surname_counts[surname] += 1
    else:
        surname_counts[surname] = 1

total_same_surname = sum(count - 1 for count in surname_counts.values())
print(total_same_surname)

# Список всех сотрудников (Имя и Фамилию) в порядке возрастания их зарплаты
sorted_staff = sorted(staff, key=lambda e: e['salary'])
for employee in sorted_staff:
    print(f"{employee['name']} {employee['surname']}")
