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
max_salary_person = 0
max_salary = staff[0]["salary"]
for num, person in enumerate(staff):
    if person["salary"] > max_salary:
        max_salary_person = num
        max_salary = person["salary"]

print(staff[max_salary_person]["name"], staff[max_salary_person]["surname"])

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

min_salary_person = 0
min_salary = staff[0]["salary"]
for num, person in enumerate(staff):
    if person["salary"] < min_salary:
        min_salary_person = num
        min_salary = person["salary"]

print(staff[min_salary_person]["name"], staff[min_salary_person]["surname"])

print("Среднеарифметическая зарплата всех сотрудников:")
summ = 0
for person in staff:
    summ += person["salary"]

print(f"{summ/len(staff):.02f}")

print("Количество однофамильцев в организации:")
surnames = []
for person in staff:
    surnames.append(person["surname"])

same_surnames = 0

for surname in surnames:
    num = surnames.count(surname)
    if num > 1:
        same_surnames +=1

print(same_surnames)

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

staff_temp = staff  # Исходный словарь оставляем без изменений
while len(staff_temp) > 0:
    min_salary_person = 0
    min_salary = staff_temp[0]["salary"]
    for num, person in enumerate(staff_temp):
        if person["salary"] < min_salary:
            min_salary_person = num
            min_salary = person["salary"]

    print(staff_temp[min_salary_person]["name"],
          staff_temp[min_salary_person]["surname"])
    
    staff_temp.pop(min_salary_person)
