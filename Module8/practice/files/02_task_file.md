## "Обработка файла <Лимерики>"

### Задание

Дан файл [data/limericks.txt](data/limericks.txt) с лимериками(короткими стихотворениями)

Выведите содержимое файла в новый файл **limericks_clean.txt**, удалив все символы точки из исходного файла

### Формат входных данных

Дан текстовый файл

### Формат выходных данных

Вывести содержимое исходного файла в новый, удалив все символы точек.

### Решение задачи

```python
path = "limericks.txt"
file_origin = open(path, "r", encoding="utf-8")
file_new = open("limericks_clean.txt", "w", encoding="utf-8")
for line in file_origin:
    file_new.write(line.replace('.', ''))
file_new.close()
file_origin.close()
```

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Для начала, выведите содержимое файла в консоль(терминал), чтобы убедиться что все работает без ошибок.
</details>

<details>
<summary>Подсказка-2</summary>
Работайте с файлом построчно:

Прочитали строку --> Удалили из нее символы точек --> Записали в новый файл
</details>

<details>
<summary>Подсказка-3</summary>
Для удаления символов из строки воспользуйтесь строковым методом .replace(".", "")
</details>
