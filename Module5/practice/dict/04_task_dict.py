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
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")

max_salary = staff[0]["salary"]
max_salary_staff = staff[0]
for item in staff:
    # print(item)
    if float(item["salary"]) > max_salary:
        max_salary = float(item["salary"])
        max_salary_staff = item
print(f"{max_salary_staff['surname']} {max_salary_staff['name']} have max salary {max_salary_staff['salary']}")

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")
min_salary = staff[0]["salary"]
min_salary_staff = staff[0]
for item in staff:
    # print(item)
    if float(item["salary"]) < min_salary:
        min_salary = float(item["salary"])
        min_salary_staff = item
print(f"{min_salary_staff['surname']} {min_salary_staff['name']} have min salary {min_salary_staff['salary']}")

print("Среднеарифметическую зарплату всех сотрудников")

summ_salary = 0
for item in staff:
    summ_salary += float(item["salary"])
# print(len(staff))
# print(summ_salary)
print(summ_salary / len(staff))

print("Количество однофамильцев в организации")
counter = 0
for num, item in enumerate(staff, 1):
    for num_incl, item_incl in enumerate(staff, 1):
        if num != num_incl and item["surname"] == item_incl["surname"]:
            counter += 1
print(counter / 2)  # same pairs

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

staff_pre_sorted = staff
staff_sorted = []
while len(staff_pre_sorted) > 0:
    min_salary = float(staff_pre_sorted[0]["salary"])
    min_salary_staff = staff_pre_sorted[0]
    min_salary_staff_index = 0
    for num, item in enumerate(staff_pre_sorted, 0):
        if float(item["salary"]) < min_salary:
            min_salary = float(item["salary"])
            min_salary_staff = item
            min_salary_staff_index = num
    staff_sorted.append(min_salary_staff)
    staff_pre_sorted.pop(min_salary_staff_index)

print(staff_sorted)
