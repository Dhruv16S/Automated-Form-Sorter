import tkinter
from tkinter.constants import END, RIGHT, Y
import openpyxl
from tkinter import Scrollbar, filedialog
from PIL import Image, ImageTk
from selenium import webdriver
h = 500; w = 700
window = tkinter.Tk()
ws = window.winfo_screenwidth() 
hs = window.winfo_screenheight() 
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
    class TkinterReturns_Form:
        def __init__(self):
            self.column = 0
        def Field_Selected(self,event):
            self.column = self.Sheet_Parameters[self.Fields_available.get(self.Fields_available.curselection())]
            Creating_Files(self.column)

        def Open_Drive(self):
            chrome_driver_path = "C:/Chrome Driver/chromedriver"
            driver = webdriver.Chrome(executable_path = chrome_driver_path)
            driver.get("https://accounts.google.com/signin/v2/identifier?service=writely&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            login = driver.find_element_by_id("identifierId")
            emailid = "dscuderiaferrari@gmail.com"
            login.send_keys(emailid)
            next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
            next_button.click()

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

    fields = TkinterReturns_Form()
    browse_Button = tkinter.Button(text = 'Browse', width = 6, command=fields.browse_file, borderwidth = 0).place(x = 400, y = 250)
    download_Button = tkinter.Button(text = "Download from Drive",command = fields.Open_Drive, borderwidth = 0).place(x = 600, y = 250)

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
    
def Send_Mails():
    Remove()
    class TkinterReturns_Mail:
        def __init__(self):
            self.file_path = "../"

    def Browse_File():
        if file_name.get(1.0,END) != "":
            file_name.delete(1.0,END)
        setattr(mails, "file_path", filedialog.askopenfilename(filetypes = (("All files", "*"), ("Template files", "*.type"))))
        file_name.insert(END, f"{mails.file_path}")
        workbook = openpyxl.load_workbook(mails.file_path)
        sheet = workbook.active
        col = sheet.max_column
        field_list = []
        for i in range(1, col + 1):
            field_list.append(sheet.cell(row = 1, column = i).value)
        setattr(mails, "fields_available", field_list)
        for name in mails.fields_available:
            displaying_fields.insert(END, u'\u2022 {}\n'.format(name))

    mails = TkinterReturns_Mail()
    scroll = tkinter.Scrollbar()
    scroll.place(x = 260, y = 150) 
    browsed_file = tkinter.Button(text = "Browse Files : ", borderwidth = 0, command = Browse_File)
    browsed_file.place(x = 50, y = 100)
    file_name = tkinter.Text(height = 1, width = 80, font = ("Times New Roman", 8), borderwidth = 0)
    file_name.place(x = 140, y = 100)
    text_label = tkinter.Label(text = "The following fields were identified from The Excel Sheet : ").place(x = 50, y = 120)
    displaying_fields = tkinter.Text(height = 5, width = 35, borderwidth = 0, font = ("Times New Roman", 10))
    displaying_fields.place(x = 50, y = 150)
    displaying_fields.config(yscrollcommand=scroll.set)
    scroll.config(command=displaying_fields.yview)
    subject_label = tkinter.Label(text = "Subject : ").place(x = 50, y = 245)
    subject = tkinter.Text(height = 1, width = 80, font = ("Times New Roman", 8), borderwidth = 0)
    subject.place(x = 140, y = 250)
    fromaddress_label = tkinter.Label(text = "From : ").place(x = 300, y = 160)
    subject = tkinter.Text(height = 1, width = 30, font = ("Times New Roman", 8), borderwidth = 0)
    subject.place(x = 350, y = 163)
    toaddress_label = tkinter.Label(text = "To : ").place(x = 300, y = 190)
    subject = tkinter.Text(height = 1, width = 30, font = ("Times New Roman", 8), borderwidth = 0)
    subject.place(x = 350, y = 193)
    # help_to = Balloon(window)
    # help_to.bind_widget(toaddress_label, balloonmsg = f"Enter the field of the Excel file from where you wish to extract the email ids.")

sort_buttonimg = Image.open("Images/Excel_Icon.png").resize((125, 125))
sort_buttonimg = ImageTk.PhotoImage(sort_buttonimg)
sort_button = tkinter.Button(image = sort_buttonimg, borderwidth = 0, command = Form_Sorting).place(x = 90, y = 100)
sort_buttonlabel = tkinter.Label(text = "Sort Forms").place(x = 135, y = 220)

mail_buttonimg = Image.open("Images/Email.png").resize((125, 125))
mail_buttonimg = ImageTk.PhotoImage(mail_buttonimg)
mail_button = tkinter.Button(image = mail_buttonimg, borderwidth = 0, command = Send_Mails).place(x = 100, y = 280)
mail_buttonlabel = tkinter.Label(text = "Send Mails").place(x = 135, y = 400)

# user_img = Image.open("Images/User.png").resize((200, 200))
# user_img = ImageTk.PhotoImage(user_img)
# user_label = tkinter.Label(image = user_img).place(x = 450, y = 50)
# text = tkinter.Label(text = "Form\n     Manager", font = ("Times New Roman", 30, "bold")).place(x = 425, y = 250)
# Username = "JohnDoe"
# date = "14.3.2021"
# user_info = Balloon(window)
# user_info.bind_widget(user_label, balloonmsg = f"{Username}\nLast Login - {date}")

window.mainloop()



