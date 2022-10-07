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

names_salary = {f"{employe['name']} {employe['surname']}": employe['salary'] for employe in staff}

salaries = names_salary.values()
max_salary = max(salaries)
names = [name for name, salary in names_salary.items() if salary == max_salary]
print(f"Имя и Фамилию сотрудника с самой высокой зарплатой: {', '.join(names)}")

min_salary = min(salaries)
names = [name for name, salary in names_salary.items() if salary == min_salary]
print(f"Имя и Фамилию сотрудника с самой низкой зарплатой: {', '.join(names)}")

total = 0
for salary in salaries:
    total += salary
print(f"Среднеарифметическая зарплата всех сотрудников: {total / len(salaries):.2f}")

namesake = {}
for employe in staff:
    if employe['surname'] in namesake:
        namesake[employe['surname']] += 1
    else:
        namesake[employe['surname']] = 1

namesake_number = 0
for _ , number in namesake.items():
    if number > 1:
        namesake_number += number
print(f"Количество однофамильцев в организации: {namesake_number}")

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")
names_salary_sorted = sorted(names_salary.items(), key=lambda x: x[-1])
for name, salary in names_salary_sorted:
    print(f"{name} {salary}")
