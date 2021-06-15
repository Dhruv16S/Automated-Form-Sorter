
# Get access to drive link
# Read number of rows, then access heading of each column. According to users interest, choose what to select

import openpyxl
import tkinter

class FieldNumber:
    def __init__(self):
        self.column = 0
    def Field_Selected(self,event):
        self.column = Sheet_Parameters[Fields_available.get(Fields_available.curselection())]
        Creating_Files(self.column)

wb = openpyxl.load_workbook("Sample.xlsx")   # Enter file name here
window = tkinter.Tk()
window.minsize(height = 500, width = 500)


#BE CAREFUL IF THE FILE ALREADY EXISTS, IT ADDS ONTO IT


sheet = wb['Sheet1']   #Enter sheet name here
Sheet_Parameters = {}
column = sheet.max_column
row = sheet.max_row

for i in range(1, column + 1):
    Sheet_Parameters[sheet.cell(row = 1, column = i).value] = i

fields = FieldNumber()

Fields_available = tkinter.Listbox(height = len(Sheet_Parameters))
for key, value in Sheet_Parameters.items():
    Fields_available.insert(value, key)
Fields_available.bind("<<ListboxSelect>>",fields.Field_Selected)
Fields_available.pack()

#choice = input("The following fields were obtained how would you like to classify the form : ?")
# operating_column = Sheet_Parameters[choice]
# operating_column = fields.column
# print(operating_column)

def Creating_Files(operating_column):
    for i in range(2, row + 1):    
        file_name = sheet.cell(i, operating_column).value.split(",")      #Do I want to split on the basis of number also....
        for field_types in file_name:
            try:
                new_wb = openpyxl.load_workbook(f"{field_types}.xlsx")
            except FileNotFoundError:
                new_wb = openpyxl.Workbook()
            new_sheet = new_wb.active
            new_rows = new_sheet.max_row + 1
            for j in range(1, column + 1):
                new_sheet.cell(new_rows,j,value = sheet.cell(i,j).value)    
            new_wb.save(f"{field_types}.xlsx")
window.mainloop()