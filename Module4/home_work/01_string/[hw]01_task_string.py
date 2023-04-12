# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = "sgh,ethy.eethuy,eeyuetuu,etueu,etuu,dhg.eryey."

num_commas = text.count(",")
num_dots = text.count(".")
print(f"Количество точек: {num_dots}")
print(f"Количество запятых: {num_commas}")
if num_dots == num_commas:
    print("Количество одинаково")
