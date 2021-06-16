# import tkinter
# class FieldNumber:
#     def __init__(self):
#         self.column = 0
#     def Field_Selected(self,event):
#         self.column = Sheet_Parameters[Fields_available.get(Fields_available.curselection())]
#         # print(self.column)

# def Sample():
#     print(fields.column)

# Sheet_Parameters = {"Name" : 1, "Email" : 2, "Phone" : 3, "Choice" : 4, "Roll" : 5} 
# window = tkinter.Tk()
# window.minsize(height = 500, width = 500)
# fields = FieldNumber()
# Fields_available = tkinter.Listbox(height = len(Sheet_Parameters))
# for key, value in Sheet_Parameters.items():
#     Fields_available.insert(value, key)
# Fields_available.bind("<<ListboxSelect>>",fields.Field_Selected)
# Fields_available.pack()
# button = tkinter.Button(text = "Click", command = Sample)
# button.pack()
# window.mainloop()

WHITE = "#FFFFFF"

import tkinter
from tkinter.constants import LEFT
window = tkinter.Tk()
window.minsize(height = 500, width = 700)
window.config(bg = WHITE)
def Print():
    print("here")

file = tkinter.PhotoImage(file = "TestImage.png")

button = tkinter.Button(text = "Hello",image = file,command=Print,borderwidth=0)
button.pack()
window.mainloop()
import os
# print(os.listdir("../../"))
files_available = os.listdir("../")
print(files_available)
# files_available = os.walk("../../../../")
# for i,j,k in files_available:
#     for filenames in k:
#         if filenames.endswith(".xlsx"):
#             print(filenames)
    
