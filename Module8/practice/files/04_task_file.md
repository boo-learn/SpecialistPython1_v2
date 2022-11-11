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

```python
salary_surpass = 60000
f_read = open("salaries.txt", 'r', encoding="utf-8")
first_line = True
for line in f_read:
    if first_line:
        first_line = False
    else:
        element_list = line.split()
        surname = element_list[0]
        name = element_list[1]
        second_name = element_list[2]
        salary = element_list[3]

        if float(salary) > salary_surpass:
            f_write = open("highly_paid.txt", 'a', encoding="utf-8")
            f_write.write(f"{surname} {name[0]}. {second_name[0]}.\n")
            f_write.close()
        
f_read.close()
```

---
