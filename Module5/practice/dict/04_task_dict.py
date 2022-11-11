# Данные о сотрудниках в программе хранятся в словаре
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
print("Имя и Фамилию сотрудника с самой высокой зарплатой: ", end="")
print("{0[name]} {0[surname]}".format(max(staff, key=lambda x: x['salary'])))

print("Имя и Фамилию сотрудника с самой низкой зарплатой: ", end="")
print("{0[name]} {0[surname]}".format(min(staff, key=lambda x: x['salary'])))

print("Среднеарифметическую зарплату всех сотрудников: ", end="")
print(round(sum(list(map(lambda x: x['salary'], staff))) / len(staff), 2))

print("Количество однофамильцев в организации")

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты:")
staff.sort(key=lambda x: x['salary'])
print(*[("   {} {}".format(el["name"], el['surname'])) for el in staff], sep="\n")
