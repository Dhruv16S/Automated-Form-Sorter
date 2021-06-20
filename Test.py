import openpyxl
wb = openpyxl.load_workbook("Sample.xlsx")
sheet = wb.active
for i in range(1, sheet.max_column + 1):
    print(sheet.cell(1,i).value)