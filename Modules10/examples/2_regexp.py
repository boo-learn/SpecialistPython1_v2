import re

# Функции

# re.match(pattern, string)
# Проверяет, соответствует ли начало строки "string" регулярному выражению "pattern".
# Например, выражению 'test' соответствует строка 'test1',
# но не соответствует строка '1test'. Возращает объект MatchObject, если строка найдена,
# или None, если не найдена.

# re.search()
# Работает аналогично re.match, но проверяет не только с начала строки,
# а сканирует строку на совпадения полностью.

# re.findall()
# Выполняет поиск всех подстрок в строке, соответствующих регулярному выражению.
# Возвращает список найденных подстрок, строки не перекрываются.
# re.split()
# re.sub()
# re.compile()

# Метасимволы
# . ^ $ * + ? { [ ] \ | ( )

# .	    Один любой символ, кроме новой строки \n.
# ?	    0 или 1 вхождение шаблона слева
# +	    1 и более вхождений шаблона слева
# *	    0 и более вхождений шаблона слева
# \w	Любая цифра или буква (\W — все, кроме буквы или цифры)
# \d	Любая цифра [0-9] (\D — все, кроме цифры)
# \s	Любой пробельный символ (\S — любой непробельный символ)
# \b	Граница слова
# [..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
# \	    Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
# ^ и $	Начало и конец строки соответственно
# {n,m}	От n до m вхождений ({,m} — от 0 до m)
# a|b	Соответствует a или b
# ()	Группирует выражение и возвращает найденный текст
# \t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно

# Сколько раз слово присутствует в строке
string = 'This is a simple test message for test'
found = re.findall(r'test', string)
print(found)

string = 'This is a simple test message for test'
string2 = 'test'

pattern1 = 'test$'
pattern2 = '^test'
pattern3 = '^test$'

print(re.search(pattern1, string) is None)  # Строка заканчивается на 'test'
print(re.match(pattern2, string) is None)  # Строка не начинается на 'test'
print(re.match(pattern3, string) is None)  # Строка не является строкой 'test'
print(re.match(pattern3, string2) is None)  # Строка является строкой 'test'

# Найти все цифры в тексте
pattern = '[0-9]+k'
string = 'If 300 spartans were so brave, so 500 spartans' \
         ' could destroy more than 10k warriors of Darius, but 15k and even 20k'
print(re.findall(pattern, string))

# Найти все диапазоны
pattern2 = '[0-9]+ *- *[0-9]+'
string2 = 'The temperature can be in range 10- 15C next week ' \
          'though it was lesser last week(4 - 9C). It was even ' \
          '-5 some time ago'
print(re.findall(pattern2, string2))


# Получим нужные данные из лога для дальнейшего анализа
log = [
    '64 bytes from localhost.localdomain (127.0.0.1): '
    'icmp_req=1 ttl=64 time=0.033 ms',
    '64 bytes from localhost.localdomain (127.0.0.1): '
    'icmp_req=2 ttl=64 time=0.034 ms',
    '64 bytes from localhost.localdomain (127.0.0.1): '
    'icmp_req=3 ttl=64 time=0.031 ms',
    '64 bytes from localhost.localdomain (127.0.0.1): '
    'icmp_req=4 ttl=64 time=0.031 ms']
pattern = re.compile('(icmp_req=[\d]+).*(time=[\d\.]+ ms)')
result = []
for line in log:
    result.append(pattern.search(line).groups())
print(result)

# Извлечем из html-кода только теги
html = '<p style="margin-left:10px;">text' \
       '<b class="super-bold">bold text</b>.</p>'
pattern = '<[^>]+>'
print(re.findall(pattern, html))


# Распарсить url
url = 'https://geekbrains.ru/streams/457/lessons/4026'

pattern = r"(/{1}[\w^.]+)"

print(re.findall(pattern, url))
