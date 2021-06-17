import tkinter
import openpyxl
from tkinter import filedialog
from PIL import Image, ImageTk
h = 500; w = 700
window = tkinter.Tk()
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.title("Unified Form Manager")
window.minsize(height = h, width = w)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

def Remove():
    widgets = window.winfo_children()
    for item in widgets :
        if item.winfo_children() :
            widgets.extend(item.winfo_children())
    for item in widgets:
        item.destroy()

def Form_Sorting():
    Remove()
    class TkinterReturns:
        def __init__(self):
            self.column = 0
        def Field_Selected(self,event):
            self.column = self.Sheet_Parameters[self.Fields_available.get(self.Fields_available.curselection())]
            Creating_Files(self.column)

        def browse_file(self):
            Remove()
            setattr(fields,'name',filedialog.askopenfilename(filetypes = (("All files", "*"), ("Template files", "*.type"))))
            wb = openpyxl.load_workbook(fields.name)
            self.sheet = wb.active 
            self.Sheet_Parameters = {}
            self.column = self.sheet.max_column
            self.row = self.sheet.max_row
            for i in range(1, self.column + 1):
                self.Sheet_Parameters[self.sheet.cell(row = 1, column = i).value] = i

            label = tkinter.Label(text = "The following fields have been identified, how would you like to classify the form : ").pack()
            self.Fields_available = tkinter.Listbox(height = len(self.Sheet_Parameters), borderwidth=0)
            for key, value in self.Sheet_Parameters.items():
                self.Fields_available.insert(value, key)
                self.Fields_available.bind("<<ListboxSelect>>",fields.Field_Selected)
                self.Fields_available.pack()

    fields = TkinterReturns()
    browse_Button = tkinter.Button(text = 'Browse', width = 6, command=fields.browse_file, borderwidth = 0).pack()
        

    def Creating_Files(operating_column):
        for i in range(2, fields.row + 1):    
            choices_opted = str(fields.sheet.cell(i, operating_column).value).split(",")      #Do I want to split on the basis of number also....
            file_name = [choice.strip() for choice in choices_opted]
            for field_types in file_name:                                      
                try:
                    new_wb = openpyxl.load_workbook(f"{field_types}.xlsx")
                except FileNotFoundError:
                    new_wb = openpyxl.Workbook()
                new_sheet = new_wb.active
                new_rows = new_sheet.max_row + 1
                for j in range(1, fields.column + 1):
                    new_sheet.cell(new_rows,j,value = fields.sheet.cell(i,j).value)    
                    new_wb.save(f"{field_types}.xlsx")
    
sort_buttonimg = Image.open("Images/Excel_Icon.png").resize((125, 125))
sort_buttonimg = ImageTk.PhotoImage(sort_buttonimg)
sort_button = tkinter.Button(image = sort_buttonimg, borderwidth = 0, command = Form_Sorting).place(x = 90, y = 100)
sort_buttonlabel = tkinter.Label(text = "Sort Forms").place(x = 135, y = 220)

mail_buttonimg = Image.open("Images/Email.png").resize((125, 125))
mail_buttonimg = ImageTk.PhotoImage(mail_buttonimg)
mail_button = tkinter.Button(image = mail_buttonimg, borderwidth = 0).place(x = 100, y = 280)
mail_buttonlabel = tkinter.Label(text = "Send Mails").place(x = 135, y = 400)

window.mainloop()