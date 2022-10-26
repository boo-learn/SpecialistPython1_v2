# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
n=int(input("n:"))
sum=0
for numb in range(-100, 100, (100//n)*2):
    if numb>0 and numb%2==0:
        sum=sum+numb
    print(numb)
print("Сумма:",sum)
