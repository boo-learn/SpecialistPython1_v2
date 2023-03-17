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

# TODO: your code here
salary_max = 0
person_max_salary = {}
for num, staff_person in enumerate(staff):
    if staff_person["salary"] > salary_max:
        salary_max = staff_person["salary"]
        person_max_salary = staff[num]
print(person_max_salary.get("name"), person_max_salary.get("surname"))

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

# TODO: your code here
salary_min = float("inf")
person_min_salary = {}
for num, staff_person in enumerate(staff):
    if staff_person["salary"] < salary_min:
        salary_min = staff_person["salary"]
        person_min_salary = staff[num]
print(person_min_salary.get("name"), person_min_salary.get("surname"))

print("Среднеарифметическую зарплату всех сотрудников")

# TODO: your code here
total_salary = 0
for staff_person in staff:
    total_salary += staff_person.get("salary")
print(total_salary / len(staff))

print("Количество однофамильцев в организации")

# TODO: your code here
surname_dict = {}
for staff_person in staff:
    if staff_person.get("surname") in surname_dict:
        index = surname_dict.get(staff_person.get("surname")) + 1
        surname_dict.update({staff_person.get("surname"): index})
    else:
        surname_dict[(staff_person.get("surname"))] = 1

print(surname_dict)

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

# TODO: your code here

# без использования рекурсии я сортировки не знаю, поэтому воспользуюсь лямба выражением
print(sorted(staff, key=lambda element: element["salary"]))
