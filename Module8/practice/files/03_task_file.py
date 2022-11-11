path = "sold.txt"
f = open(path, "r")
prices = []
str_list = []
string = ""
total_cost = 0
max_cost = 0
min_cost = 0

for line in f:
    res_line = line.replace("\n","")
    str_list.append(res_line)
for day in str_list:
    string = " ".join(str_list)

prices = string.split()
res_prices = [float(cost) for cost in prices]

max_cost = max(res_prices)
min_cost = min(res_prices)
total_cost = sum(res_prices)


print(f"Общая сумма товаров: {total_cost:.2f}")
print(f"Самый дешевый товар: {min_cost}")
print(f"Самый дорогой товар: {max_cost}")

f.close()
