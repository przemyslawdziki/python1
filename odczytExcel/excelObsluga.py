import openpyxl

wb = openpyxl.load_workbook('STYCZEN.xlsm')
sheet = wb.active
data = []

file = open("lista.txt", "w")
j = 0
for row in sheet.iter_rows(values_only=True):
    row_data = []
    i = 0
    #j = 0
    rep = ""
    for cell in row:
        if i < 35:
            # if i == 2:
            #     rep = ""
            #     file.write(str(rep))
            # if cell != None:
            rep = str(cell) + ";"
            file.write(str(rep))
        i += 1
        j += 1
        if j == 105:
            rep = "\n"
            file.write(rep)
            j = 0
    # data.append(row_data)
file.close()

plik = open("lista.txt", "r")
lista = plik.readlines()

for row in lista:
    for iter in row:
        if iter == None:
            lista.pop(iter)




# tablica = []
# for row in range(2, len(data)):
#     #print(data[row], end="\n")
#     for item in data[row]:
#         if item != None:
#             tablica.append(item)
#
#


input("Nacisnij Enter aby zakończyć.")



