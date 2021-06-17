# import tkinter as tk

# def clear():
#     root.destroy()

# root = tk.Tk() # create a Tk root window

# w = 700 # width for the Tk root
# h = 500 # height for the Tk root

# # get screen width and height
# ws = root.winfo_screenwidth() # width of the screen
# hs = root.winfo_screenheight() # height of the screen

# # calculate x and y coordinates for the Tk root window
# x = (ws/2) - (w/2)
# y = (hs/2) - (h/2)

# # set the dimensions of the screen 
# # and where it is placed
# root.geometry('%dx%d+%d+%d' % (w, h, x, y))
# root.minsize(height = 500, width=700)
# button = tk.Button(text = "Click", command = clear)
# button.pack()
# root.mainloop() # starts the mainloop


# root = tk.Tk()
# root.geometry('%dx%d+%d+%d' % (w, h, x, y))
# root.minsize(height = 500, width=700)
# root.mainloop() # starts the mainloop



import openpyxl
import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk

def Create():
    global window
    window = tkinter.Tk()
    window.title("Unified Form Manager")
    window.minsize(height = 500, width = 700)
    w = 700 # width for the Tk root
    h = 500 # height for the Tk root
    ws = window.winfo_screenwidth() # width of the screen
    hs = window.winfo_screenheight() # height of the screen
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.minsize(height = h, width = w)
    return window

def Clear():
    window.destroy()


# user_image = Image.open("Username.png")
# user_image = user_image.resize((25, 25))
# user_image = ImageTk.PhotoImage(user_image)
# label = tkinter.Label(image = user_image)
# label.place(x = 670, y = 0)

def Form_Sorting():
    Clear()
    class TkinterReturns:
        def __init__(self):
            self.column = 0
            self.name = "."
        def Field_Selected(self,event):
            self.column = Sheet_Parameters[Fields_available.get(Fields_available.curselection())]
            Creating_Files(self.column)
        def browse_file(self):
            window.destroy()
            self.name = filedialog.askopenfilename(filetypes = (("All files", "*"), ("Template files", "*.type")))
            

    fields = TkinterReturns()

    window = Create()
    browse_Button = tkinter.Button(master = window, text = 'Browse', width = 6, command=fields.browse_file, borderwidth = 0)
    browse_Button.pack(side=tkinter.LEFT, padx = 2, pady=2)
    window.mainloop()


    wb = openpyxl.load_workbook(fields.name)   
    window = Create()


    sheet = wb.active 
    Sheet_Parameters = {}
    column = sheet.max_column
    row = sheet.max_row
    for i in range(1, column + 1):
        Sheet_Parameters[sheet.cell(row = 1, column = i).value] = i


    label = tkinter.Label(window, text = "The following fields have been identified, how would you like to classify the form : ")
    label.pack()
    Fields_available = tkinter.Listbox(height = len(Sheet_Parameters), borderwidth=0)
    for key, value in Sheet_Parameters.items():
        Fields_available.insert(value, key)
        Fields_available.bind("<<ListboxSelect>>",fields.Field_Selected)
        Fields_available.pack()

    def Creating_Files(operating_column):
        for i in range(2, row + 1):    
            choices_opted = str(sheet.cell(i, operating_column).value).split(",")      #Do I want to split on the basis of number also....
            file_name = [choice.strip() for choice in choices_opted]
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



sort_buttonimg = Image.open("Excel_icon.png")
sort_buttonimg = sort_buttonimg.resize((125, 125))
sort_buttonimg = ImageTk.PhotoImage(sort_buttonimg)
sort_button = tkinter.Button(image = sort_buttonimg, borderwidth = 0, command = Form_Sorting)
sort_button.place(x = 100, y = 100)
sort_buttonlabel = tkinter.Label(text = "Sort Forms")
sort_buttonlabel.place(x = 135, y = 220)

mail_buttonimg = Image.open("automated_email.png")
mail_buttonimg = mail_buttonimg.resize((125, 125))
mail_buttonimg = ImageTk.PhotoImage(mail_buttonimg)
mail_button = tkinter.Button(image = mail_buttonimg, borderwidth = 0)
mail_button.place(x = 300, y = 100)
mail_buttonlabel = tkinter.Label(text = "Send Mails")
mail_buttonlabel.place(x = 335, y = 220)

window.mainloop()
