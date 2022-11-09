# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = ...

a = str("фыпафвплдп.фыалтыаыфыат,дфыоатр,фыд...аофыадлтфыдафыдао,ф")
point = len(a.split("."))-1
comma = len(a.split(","))-1
if point > comma:
    print(f"{point} > {comma}")
    
elif point < comma:
    print(f"{point} < {comma}")

else:
    print(point, comma)
