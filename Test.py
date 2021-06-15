import tkinter
class FieldNumber:
    def __init__(self):
        self.column = 0
    def Field_Selected(self,event):
        self.column = Sheet_Parameters[Fields_available.get(Fields_available.curselection())]
        # print(self.column)

def Sample():
    print(fields.column)

Sheet_Parameters = {"Name" : 1, "Email" : 2, "Phone" : 3, "Choice" : 4, "Roll" : 5} 
window = tkinter.Tk()
window.minsize(height = 500, width = 500)
fields = FieldNumber()
Fields_available = tkinter.Listbox(height = len(Sheet_Parameters))
for key, value in Sheet_Parameters.items():
    Fields_available.insert(value, key)
Fields_available.bind("<<ListboxSelect>>",fields.Field_Selected)
Fields_available.pack()
button = tkinter.Button(text = "Click", command = Sample)
button.pack()
window.mainloop()
