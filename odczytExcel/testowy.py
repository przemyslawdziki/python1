list = [2,4,6,8,3,5]

a= sum(list)

print(a)
suma = 0

i=0
for i in range(len(list)):
    print(list[i])
    suma += list[i]
    i += 1

print(f"Suma = {str(suma):>9s}")