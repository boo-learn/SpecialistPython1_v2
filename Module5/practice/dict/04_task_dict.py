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
highest_salary_employee = max(staff, key=lambda x: x['salary'])
print(
    f"Имя и Фамилию сотрудника с самой высокой зарплатой: {highest_salary_employee['name']} {highest_salary_employee['surname']}")

lowest_salary_employee = min(staff, key=lambda x: x['salary'])
print(
    f"Имя и Фамилию сотрудника с самой низкой зарплатой: {lowest_salary_employee['name']} {lowest_salary_employee['surname']}")

average_salary = sum(employee['salary'] for employee in staff) / len(staff)
print(f"Среднеарифметическую зарплату всех сотрудников: {average_salary:.2f}")

surnames = [employee['surname'] for employee in staff]
unique_surnames = set(surnames)
surname_counts = [surnames.count(surname) for surname in unique_surnames]
same_surname_count = sum(count - 1 for count in surname_counts)
print(f"Количество однофамильцев в организации: {same_surname_count}")

sorted_staff = sorted(staff, key=lambda x: x['salary'])
print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты:")
for employee in sorted_staff:
    print(f"{employee['name']} {employee['surname']}")
