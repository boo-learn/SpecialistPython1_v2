## "Высокооплачиваемые сотрудники"

### Задание
В файле [data/salaries.txt](data/salaries.txt) даны зарплаты сотрудников.

Выведите всех сотрудников в файл highly_paid.txt, зарплаты которых превышают 60000. \
Формат вывода смотри в "Формат выходных данных"

### Формат входных данных

Дан текстовый файл. \
В первой строке указаны названия параметров сотрудника. \
В каждой следующей строке дана информация о сотруднике.

### Формат выходных данных

Записать информацию в файл highly_paid.txt о сотрудниках с зарплатой выше 60000.

Сотрудников вывести в формате: Фамилия И.О., \
например: **Иванов И.П.** (зарплаты в выходной файл не записывать)

### Решение задачи

input_data = "salaries.txt"
output_data = "highly_paid.txt"
SALARY_LIMIT = 60000

f_in = open(input_data, "r", encoding="utf-8")
f_out = open(output_data, "w", encoding="utf-8")

for num, line in enumerate(f_in):
    if num > 0:
        temp_line = line.split()
        if int(temp_line[3]) > SALARY_LIMIT:
            f_out.write(f"{temp_line[0]} {temp_line[1][:1]}.{temp_line[2][:1]}.\n")

f_in.close()
f_out.close()


---
