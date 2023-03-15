## "С большой буквы"

### Задание

Для регистрации на сайте, пользователи часто вводят Имя и Фамилию с маленькой буквы. \
Напишите мини-программу, которая будет запрашивать у пользователя имя и фамилию и заменять первые буквы буквами в верхнем регистре. \
Измененные данные(имя и фамилию) вывести на экран.

### Формат входных данных

Даны две строки, имя и фамилия.

### Формат выходных данных

Вывести исходные строки, заменив первые буквы имени и фамилии символами в верхнем регистре(большими буквами).

### Решение задачи

```python
name = input("Имя: ")
surname = input("Фамилия: ")

name_first_letter = name[0]
name_other_letters = name[1:]
name_first_letter_up = name_first_letter.upper()

surname_first_letter = surname[0]
surname_other_letters = surname[1:]
surname_first_letter_up = surname_first_letter.upper()

print(name_first_letter_up + name_other_letters, surname_first_letter_up + surname_other_letters)
```

---

<details>
<summary>Подсказка-1</summary>
Для решения задачи найдите подходящий метод строки.
</details>
