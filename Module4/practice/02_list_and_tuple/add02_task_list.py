# Пользователь вводит на экран дату в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.

# Подсказка: создайте списки с названием дней и названиями месяцев
# Примечание: для экономии времени, можно ограничить номер дня десятью.
# Примечание: склонениями названий можно принебречь

inp_date = "23.11.2013"
months = ("January", "February", "March", "April", "May", "June"
          , "July", "August", "September", "October", "November", "December")
days = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"
        , "ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth"
        , "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth"
        , "twenty-first", "twenty-second", "twenty-third", "twenty-fourth", "twenty-fifth"
        , "twenty-sixth", "twenty-seventh", "twenty-eighth", "twenty-ninth", "thirtieth", "thirty-first")

inp_date_ar = inp_date.split(".")
#print(int(inp_date_ar[0]))
day = days[int(inp_date_ar[0])-1]
month = months[int(inp_date_ar[1])-1]
#print(day.title())
#print(month.title())
string = "Human readable: "+day.title()+' of '+month.title()+" "+inp_date_ar[2]+' year'
print(string)
