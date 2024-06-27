import openpyxl

protype=[[]]
protype.append(["Function Prototype", "Unique ID"])
with open("header.h", 'r') as file:
    i=0
    for line in file:
        line = line.strip()
        protype.append([line,"IDX"+str(i)])
        i=i+1


workbook = openpyxl.load_workbook("test.xlsx")
sheet=workbook.active
sheet.delete_cols(0,100)
sheet.delete_cols(1,100)
sheet.insert_rows(0,-2)
for i in protype:
    sheet.append(i)

workbook.save("test.xlsx")  
