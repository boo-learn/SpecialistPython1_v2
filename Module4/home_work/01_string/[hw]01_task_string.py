# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = "...  , ,.....,,,,,"
point_cnt = text.count(".")
comma_cnt = text.count(",")
# print(point_cnt,comma_cnt)
if point_cnt > comma_cnt:
    print("You have more points (.) here ")
elif point_cnt == comma_cnt:
    print("Same count")
else:
    print("You have more comma (,) here")
