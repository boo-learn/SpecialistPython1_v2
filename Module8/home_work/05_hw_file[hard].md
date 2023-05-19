## "Обработка списка фруктов"

### Задание

Дана ведомость расчета заработной платы [data/workers.txt](data/workers.txt).

Рассчитайте зарплату всех работников, зная что они получат полный оклад, если отработают норму часов. \
Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально, \
а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме. \
Кол-во часов, которые были отработаны, указаны в файле ["data/hours_of.txt](data/hours_of.txt)

### Формат входных данных

Дано два текстовых файла. Один с информацией о сотрудниках, второй с количеством отработанных часов.

Гарантируется, что каждый сотрудник имеет уникальную фамилию(однофамильцев нет).

### Формат выходных данных

Выведите зарплату сотрудников с учетом переработки и недоработки.

### Решение задачи

f = open("data/workers.txt", "r", encoding="UTF-8")

workers = []

first = True
for line in f:
    if first:
        first = False
    else:
        if line.strip() != "":
            workers.append(line.strip().split())
f.close()

f = open("data/hours_of.txt", "r", encoding="UTF-8")

hours_of = []

first = True
for line in f:
    if first:
        first = False
    else:
        if line.strip() != "":
            hours_of.append(line.strip().split())
f.close()

for worker in workers:
    salary = 0.00
    for hours_worker in hours_of:
        if hours_worker[0] == worker[0] and hours_worker[1] == worker[1]:
            standard_hours = int(worker[4])
            standard_salary = int(worker[2])
            worked_out = int(hours_worker[2])
            double_hour_cost = standard_salary / standard_hours * 2
            if worked_out > standard_hours:
                salary = round(standard_salary + (worked_out - standard_hours) * double_hour_cost, 2)
            else:
                salary = round(standard_salary * worked_out / standard_hours, 2)
    print(f"{worker[0]:<10} {worker[1]:<10} {salary:>10.2f}")
