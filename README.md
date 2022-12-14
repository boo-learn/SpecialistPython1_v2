## План по курсу "Python-1"

### Модуль 1: Знакомство с python (4 часа)

1. Введение в python
    - Краткая история языка
    - Сферы применения языка
    - Версии языка python (2.x, 3.x)
    - Установка интерпретатора
    - Принцип работы интерпретатора
1. Запуск первой программы
    - Hello World. Запуск с помощью интерпретатора
1. Линейные программы
    - Арифметические операции(выражения)
    - Переменные
    - Базовые типы данных(int, float, str)
    - Ввод/вывод данных
    - Преобразование типов. Функции преобразования
1. Практика "решение линейных задач"

### Модуль 2: Операторы ветвления (4 часа)

1. Логические операции
    - Операции сравнения (> < == !=)
    - Тип bool
1. Ветвление
    - Операторы ветвления(if else)
    - Отступы как операторные скобки
    - Составные условия (and or)
    - Вложенные ветвления
    - Полное ветвление (if elif else)
    - Функция преобразования bool(). (if a: --> if bool(a):)
1. Практическая работа "Задачи на ветвления"

### Модуль 3: Цикл while (4 часа)

1. Циклы
    - Синтаксис цикла while
    - Переменные счетчики (i = i + 1)
    - Операции сокращенного присваивания (i += 1)
    - Прерывание(break) и продолжение(continue) цикла
1. Классические алгоритмы на циклах
    - Выполнение цикла n раз
    - Вывод арифметический/геометрической последовательностей
    - Вывод фигур ASCII-символами
1. Практическая работа "Задачи на циклах"


### Модуль 4: Структуры данных Часть-1(4 часа)

1. Строки
    - Строка - неизменяемая последовательность символов
    - Операции со троками
        * Обращение по индексам
        * Срезы
        * Конкатенация и мультипликация
    - Методы строк
    - Практическая работа "Обработка строк"
1. Списки и кортежи
    - Список - изменяемая последовательность произвольных типов
    - Операции со списками
        * Создание списков
        * Обращение по индексам
        * Срезы
        * Конкатенация и мультипликация
    - Методы списков
    - Классические алгоритмы со списками:
        * Поиск максимального/минимального элемента
        * Сумма элементов (сумма с условием)
        * Поиск количества элементов по условию
    - Практическая работа "Обработка списков"
    - Сходство и отличие списка от кортежа
1. Обход последовательностей в цикле(for in)

### Модуль 5: Структуры данных Часть-2(4 часа)

1. Словари
    - Словарь - изменяемая последовательность с доступом по ключу
    - Операции со словарями
        * Создание словарей
        * Обращение по ключам. Добавление новых пар(ключ:значение)
        * Срезы
        * Объединение словарей
        * Создание словарей из списков ключей и значений
    - Методы словарей
    - Итерация по словарю(по ключам, по значениям)
    - Практическая работа "Обработка словарей"
1. Множества
    - Понятие множества
    - Операции со множествами
    - Преобразование списков к множествам и обратно

### Модуль 6: Функции (4 часа)

1. Создание функций
    - Создание собственных функций
    - Локальные и глобальные переменные
    - Понятие "чистая функция"
1. Аргументы функции
    - Переменное количество позиционных аргументов (*args)
    - Позиционные и именованные аргументы
    - Аргументы по умолчанию
    - Переменное количество именованных аргументов (**kwargs)
1. Практическая работа "Создание и тестирование функций"

### Модуль 7.1: Практическая работа "Отработка пройденного" (2 часа)

1. Отработка пройденного
2. Решение алгоритмических задач с использованием функций

### Модуль 7.2: Модули (2 часа)

1. Подключение стандартных модулей (import, from)
1. Установка стороннего модуля. Подсистема pip
1. Практика "Создание собственного модуля"
   - Создаем модуль из функций, написанных в предыдущем модуле
   - Импортируем функции из нашего модуля, для решения микро-задач

### Модуль 8: Работа с файловой системой (4 часа)

1. Чтение/запись в файл
    - open()
    - Контекстный менеджер with
1. Работа с каталогами
   - модуль os или pathlib
1. Модуль Pickle и Json

### Модуль 9.1: Обработка исключений (2 часа)

1. Ошибки и исключения
1. Виды исключений
1. Обработка исключения
1. Выброс исключения
1. Практика "задачи с обработкой исключений"

### Модуль 9.2: Продвинутые инструменты (2 часа)

1. Оператор is
1. Функции как аргументы. Функции - объекты первого порядка
1. Генераторы списков и словарей
1. lambda-функции
1. Встроенные функции map, zip, filter

### Модуль 10: Регулярные выражения. Подведение итогов (4 часа)

1. Сырые строки
1. Синтаксис регулярных выражений
1. Применение регулярных выражений
1. Практика "Парсинг строк регулярками"