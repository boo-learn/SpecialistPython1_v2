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

min_salary = staff[0]["salary"]
min_salary_idx = 0
max_salary = staff[0]["salary"]
max_salary_idx = 0
sum_salary = 0
count = 0
namesakes = 0
for employee in staff:
    if employee["salary"] < min_salary:
        min_salary = employee["salary"]
        min_salary_idx = count
    if employee["salary"] > max_salary:
        max_salary = employee["salary"]
        max_salary_idx = count
    sum_salary += employee["salary"]
    count += 1
    for employee2 in staff:
        if employee2["surname"] == employee["surname"]:
            namesakes += 1
    namesakes -= 1

print("Имя и Фамилию сотрудника с самой высокой зарплатой: ", staff[min_salary_idx]["name"], staff[min_salary_idx]["surname"])
print("Имя и Фамилию сотрудника с самой низкой зарплатой:", staff[max_salary_idx]["name"], staff[max_salary_idx]["surname"])
print("Среднеарифметическую зарплату всех сотрудников", sum_salary / count)
print("Количество однофамильцев в организации", namesakes)

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")
staff.sort(key=lambda x: x["salary"])
for employee in staff:
    print(employee["name"], employee["surname"])
