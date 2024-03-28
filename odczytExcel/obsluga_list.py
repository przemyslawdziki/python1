import openpyxl

wb = openpyxl.load_workbook('STYCZEN.xlsm')
sheet = wb.active
data = []

file = open("lista.txt", "w")

for row in sheet.iter_rows(values_only=True):
    row_data = []
    i = 0
    for cell in row:
        if i < 35 or cell != None:
            rep = str(cell) + ";"
            file.write(str(rep))
        i += 1
file.close()



