
# Get access to drive link
# Read number of rows, then access heading of each column. According to users interest, choose what to select

import openpyxl
workbook = openpyxl.load_workbook("Sample.xlsx")   # Enter file name here
sheet = workbook["Sheet"]   #Enter sheet name here
Sheet_Parameters = {}
column = sheet.max_column
for i in range(1, column + 1):
    Sheet_Parameters[sheet.cell(row = 1, column = i).value] = column

print(Sheet_Parameters)
