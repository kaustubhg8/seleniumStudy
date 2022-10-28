import openpyxl

path = "D:\scrap\Book2.xlsx"

wb = openpyxl.load_workbook(path)
sheet = wb.active
for r in range(1,6):
    for c in range(1,5):
        sheet.cell(row=r,column=c).value="Welcome"


wb.save(path)