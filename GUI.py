import tkinter
from tkinter.constants import BOTTOM, END, LEFT, NE, RIGHT, SE, TOP, Y
import openpyxl
from tkinter import  filedialog
from PIL import Image, ImageTk
from selenium import webdriver
import json
import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
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

        def Fields_Received(self):
            self.fields_fromuser = self.custom_choice.get(1.0, END)
            Creating_Files(self.column)

        def Option_Selected(self):
            if self.radio_state.get() == 1:
                Creating_Files(self.column)
                if self.custom_choice.winfo_ismapped():
                    self.custom_choice.destroy()
                    self.submit_choices.destroy()
                    
            elif self.radio_state.get() == 2:
                self.custom_choice = tkinter.Text(width = 30, height = 1)
                self.custom_choice.place(x = 168, y = 345)
                self.custom_choice.focus()
                self.submit_choices = tkinter.Button(text = "Submit", command = fields.Fields_Received)
                self.submit_choices.place(x = 420,y = 342)
                
            
            
        def Field_Selected(self,event):
            self.column = self.Sheet_Parameters[self.Fields_available.get(self.Fields_available.curselection())]
            self.radio_state = tkinter.IntVar()
            self.radiobutton1 = tkinter.Radiobutton(text = "Create a New Excel File for every distinct value encountered ", value = 1, variable = self.radio_state, command = fields.Option_Selected)
            self.radiobutton2 = tkinter.Radiobutton(text = "Create an Excel File for fields that contain : ", value = 2, variable = self.radio_state, command = fields.Option_Selected)
            self.radiobutton1.place(x = 168, y = 293)
            self.radiobutton2.place(x = 168, y = 315)
            self.custom_choice = tkinter.Text(width = 10, height = 1)          

        def Open_Drive(self):
            chrome_driver_path = "C:/Chrome Driver/chromedriver"
            driver = webdriver.Chrome(executable_path = chrome_driver_path)
            driver.get("https://accounts.google.com/signin/v2/identifier?service=writely&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            login = driver.find_element_by_id("identifierId")
            emailid = on_home.username
            login.send_keys(emailid)
            next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
            next_button.click()

        def browse_file(self):
            # Remove()
            setattr(fields,'name',filedialog.askopenfilename(filetypes = (("All files", "*"), ("Template files", "*.type"))))
            wb = openpyxl.load_workbook(fields.name)
            if file_name.get(1.0,END) != "":
                file_name.delete(1.0,END)
            file_name.insert(END,f"{fields.name}")
            self.sheet = wb.active 
            self.Sheet_Parameters = {}
            self.column = self.sheet.max_column
            self.max_column = self.sheet.max_column
            self.row = self.sheet.max_row
            for i in range(1, self.column + 1):
                self.Sheet_Parameters[self.sheet.cell(row = 1, column = i).value] = i

            label = tkinter.Label(text = "The following fields have been identified.\nHow would you like to classify the form : ").place(x = 40, y = 242)
            self.Fields_available = tkinter.Listbox(height = len(self.Sheet_Parameters), borderwidth=0)
            for key, value in self.Sheet_Parameters.items():
                self.Fields_available.insert(value, key)
                self.Fields_available.bind("<<ListboxSelect>>",fields.Field_Selected)
                self.Fields_available.place(x = 40, y = 290)
    fields = TkinterReturns_Form()
    fields.browse_img = Image.open("Images/Browse.png").resize((150,150))
    fields.browse_img = ImageTk.PhotoImage(fields.browse_img)
    fields.browse_Button = tkinter.Button(image = fields.browse_img, command = fields.browse_file, borderwidth = 0)
    fields.browse_Button.place(x = 175, y = 40)
    browselabel = tkinter.Label(text = "Browse Files").place(x = 200, y = 175)
    fields.drive_img = Image.open("Images/GDrive.png").resize((150,150))
    fields.drive_img = ImageTk.PhotoImage(fields.drive_img)
    fields.download_Button = tkinter.Button(image = fields.drive_img, command = fields.Open_Drive,borderwidth = 0)
    fields.download_Button.place(x = 350, y = 40)
    drivelabel = tkinter.Label(text = "Download From Drive").place(x = 360, y = 175)
    openfile_label = tkinter.Label(text = "File Opened : ").place(x = 175, y = 202)
    file_name = tkinter.Text(height = 1, width = 70, font = ("Times New Roman", 8), borderwidth = 0)
    file_name.place(x = 260, y = 205)
    
    homebutton = tkinter.Button(text = "Go to home", command = on_home.MainMenu).pack(side = TOP, anchor = NE)
    loggedin = tkinter.Label(text = f"Logged in as {on_home.username}").pack(side = BOTTOM, anchor = SE)
    def Creating_Files(operating_column):
        if fields.radio_state.get() == 1:
            for i in range(2, fields.row + 1):    
                choices_opted = str(fields.sheet.cell(i, operating_column).value).split(",")      
                file_name = [choice.strip() for choice in choices_opted]
                for field_types in file_name:                                 
                    try:
                        new_wb = openpyxl.load_workbook(f"{field_types}.xlsx")
                    except FileNotFoundError:
                        new_wb = openpyxl.Workbook()
                        new_sheet_fields = new_wb.active
                        for k in range(1, fields.max_column + 1):
                            new_sheet_fields.cell(row = 1, column = k, value = fields.sheet.cell(row = 1, column = k).value)
                    new_sheet = new_wb.active
                    new_rows = new_sheet.max_row + 1
                    for j in range(1, fields.max_column + 1):
                        if j == operating_column:
                            new_sheet.cell(new_rows,j,value = field_types)
                        else:
                            new_sheet.cell(new_rows,j,value = fields.sheet.cell(i,j).value)    
                        new_wb.save(f"{field_types}.xlsx")

        else:
            users_list = fields.fields_fromuser.split(",")
            users_criteria = [choices.strip() for choices in users_list]
            users_multiplelist = fields.fields_fromuser.split(";")
            users_multiplecriteria = [choices.strip() for choices in users_multiplelist]
            for choice_name in users_multiplecriteria:
                for i in range(2, fields.row + 1):
                    choices_opted = str(fields.sheet.cell(i, operating_column).value).split(",")      
                    file_name = [choice.strip() for choice in choices_opted]
                    choice_name_indv = choice_name.split(",")
                    if set(choice_name_indv).issubset(set(file_name)):
                        excel_file = ",".join([str(characters) for characters in choice_name_indv])
                        try:
                            new_wb = openpyxl.load_workbook(f"{excel_file}.xlsx")
                        except FileNotFoundError:
                            new_wb = openpyxl.Workbook()
                            new_sheet_fields = new_wb.active
                            for k in range(1, fields.max_column + 1):
                                new_sheet_fields.cell(row = 1, column = k, value = fields.sheet.cell(row = 1, column = k).value)
                        new_sheet = new_wb.active
                        new_rows = new_sheet.max_row + 1                          
                        for j in range(1, fields.max_column + 1):
                            if j == operating_column:
                                new_sheet.cell(new_rows,j,value = excel_file)
                            else:
                                new_sheet.cell(new_rows,j,value = fields.sheet.cell(i,j).value)    
                            new_wb.save(f"{excel_file}.xlsx")

            # for choice_name in users_criteria:
            #     for i in range(2, fields.row + 1):
            #         choices_opted = str(fields.sheet.cell(i, operating_column).value).split(",")      
            #         file_name = [choice.strip() for choice in choices_opted]
            #         if choice_name in file_name:
            #             try:
            #                 new_wb = openpyxl.load_workbook(f"{choice_name}.xlsx")
            #             except FileNotFoundError:
            #                 new_wb = openpyxl.Workbook()
            #             new_sheet = new_wb.active
            #             new_rows = new_sheet.max_row + 1                          
            #             for j in range(1, fields.column + 1):
            #                 if j == operating_column:
            #                     new_sheet.cell(new_rows,j,value = choice_name)
            #                 else:
            #                     new_sheet.cell(new_rows,j,value = fields.sheet.cell(i,j).value)    
            #                 new_wb.save(f"{choice_name}.xlsx")
    
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
    subject = tkinter.Text(height = 1, width = 80, font = ("Times New Roman", 8 , "bold"), borderwidth = 0)
    subject.place(x = 140, y = 250)
    fromaddress_label = tkinter.Label(text = "From : ").place(x = 300, y = 160)
    subject = tkinter.Text(height = 1, width = 30, font = ("Times New Roman", 8), borderwidth = 0)
    subject.place(x = 350, y = 163)
    toaddress_label = tkinter.Label(text = "To : ").place(x = 300, y = 190)
    subject = tkinter.Text(height = 1, width = 30, font = ("Times New Roman", 8), borderwidth = 0)
    subject.place(x = 350, y = 193)
    homebutton = tkinter.Button(text = "Go to home", command = on_home.MainMenu).pack(side = TOP, anchor = NE)
    loggedin = tkinter.Label(text = f"Logged in as {on_home.username}").pack(side = BOTTOM, anchor = SE)
    # help_to = Balloon(window)
    # help_to.bind_widget(toaddress_label, balloonmsg = f"Enter the field of the Excel file from where you wish to extract the email ids.")


class Home:
    def HomePage(self):
        on_home.homebutton.destroy()
        self.signin_img = Image.open("Images/Signin.png")
        self.signin_img = ImageTk.PhotoImage(self.signin_img)
        self.signin_button = tkinter.Button(image = self.signin_img, borderwidth = 0, command = on_home.Clicked_Signin)
        self.signin_button.place(x = 60, y = 100)

        self.app_img = Image.open("Images/App name.png")
        self.app_img = ImageTk.PhotoImage(self.app_img)
        self.app = tkinter.Label(image = self.app_img, borderwidth = 0)
        self.app.place(x = 262, y = 100)

        self.login_img = Image.open("Images/Login.png")
        self.login_img = ImageTk.PhotoImage(self.login_img)
        self.login_button = tkinter.Button(image = self.login_img, borderwidth = 0, command = on_home.Clicked_Login)
        self.login_button.place(x = 462, y = 100)


    def MainMenu(self):
        Remove()
        on_home.homebutton.destroy()
        self.sort_buttonimg = Image.open("Images/Excel_Icon.png").resize((125, 125))
        self.sort_buttonimg = ImageTk.PhotoImage(self.sort_buttonimg)
        self.sort_button = tkinter.Button(image = self.sort_buttonimg, borderwidth = 0, command = Form_Sorting).place(x = 90, y = 100)
        self.sort_buttonlabel = tkinter.Label(text = "Sort Forms").place(x = 135, y = 220)

        self.mail_buttonimg = Image.open("Images/Email.png").resize((125, 125))
        self.mail_buttonimg = ImageTk.PhotoImage(self.mail_buttonimg)
        self.mail_button = tkinter.Button(image = self.mail_buttonimg, borderwidth = 0, command = Send_Mails).place(x = 100, y = 280)
        self.mail_buttonlabel = tkinter.Label(text = "Send Mails").place(x = 135, y = 400)

        self.loggedin = tkinter.Label(text = f"Logged in as {self.username}").pack(side = BOTTOM, anchor = SE)


    def CreatingAccount(self):
        f=open("logindetails.json","r+")
        contents = f.read()
        js = json.loads(contents)
        js.append({'username': self.username, 'password': self.password})
        f.seek(0)       
        f.write(json.dumps(js, indent=2))
        f.truncate()
        f.close()
        self.MainMenu()
    
    def CheckingForAccount(self):
        f = open("logindetails.json","r+")
        contents = f.read()
        js = json.loads(contents)
        self.email = True
        for i in range(len(js)):
            if js[i]['username'] == self.username:
                if js[i]['password'] == self.password:
                    # print("Login Successful")
                    self.email = True
                    self.MainMenu()
                else:
                    self.incorrectpassword = tkinter.Label(text = "Incorrect Password", borderwidth = 0, bg = "white", fg = "red").place(x = 110, y = 337)
                    self.passwordwidget.config(fg = "red")
                    break
            else:
                self.email = False  
        if self.email is False:
            self.incorrectemail = tkinter.Label(text = "Email does not exist, try to Sign Up",  borderwidth = 0, bg = "white", fg = "red").place(x = 110, y = 230)
            self.usernamewidget.config(fg = "red")
        f.close()

        # Need to create a button for Forgot Password

    def Submit_NewUser(self):
        self.username = self.usernamewidget.get(1.0, END).strip()
        self.password = self.passwordwidget.get(1.0, END).strip()
        self.CreatingAccount()

    def Submit_Login(self):
        self.username = self.usernamewidget.get(1.0, END).strip()
        self.password = self.passwordwidget.get(1.0, END).strip()
        self.CheckingForAccount()
    
    def Clicked_Signin(self):
        self.homebutton.destroy()
        app.destroy(); login_button.destroy()
        self.userdetails_img = Image.open("Images/UserDetails.png")
        self.userdetails_img = ImageTk.PhotoImage(self.userdetails_img)
        self.user = tkinter.Label(image = self.userdetails_img, borderwidth = 0)
        self.user.place(x = 262, y = 100)
        self.usernamewidget = tkinter.Text(height = 1, width = 25, font = ("TimesNewRoman"))
        self.usernamewidget.place(x = 310, y  = 200)
        self.passwordwidget = tkinter.Text(height = 1, width = 25, font = ("TimesNewRoman"))
        self.passwordwidget.place(x = 310, y  = 310)
        self.next = tkinter.Button(text = "Next", font = (20), borderwidth = 0, command = self.Submit_NewUser)
        self.next.place(x = 590, y = 340)
        self.homebutton = tkinter.Button(text = "Go to home", command = on_home.HomePage)
        self.homebutton.pack(side = TOP, anchor = NE)
    def Clicked_Login(self):
        self.homebutton.destroy()
        app.destroy(); signin_button.destroy()
        self.userdetails_img = Image.open("Images/UserDetails.png")
        self.userdetails_img = ImageTk.PhotoImage(self.userdetails_img)
        self.user = tkinter.Label(image = self.userdetails_img, borderwidth = 0)
        self.user.place(x = 60, y = 100)
        self.usernamewidget = tkinter.Text(height = 1, width = 25, font = ("TimesNewRoman"))
        self.usernamewidget.place(x = 110, y  = 200)
        self.passwordwidget = tkinter.Text(height = 1, width = 25, font = ("TimesNewRoman"))
        self.passwordwidget.place(x = 110, y  = 310)
        self.next = tkinter.Button(text = "Next", font = (20), borderwidth = 0, command = self.Submit_Login)
        self.next.place(x = 390, y = 340)
        self.homebutton = tkinter.Button(text = "Go to home", command = on_home.HomePage)
        self.homebutton.pack(side = TOP, anchor = NE)
on_home = Home()

signin_img = Image.open("Images/Signin.png")
signin_img = ImageTk.PhotoImage(signin_img)
signin_button = tkinter.Button(image = signin_img, borderwidth = 0, command = on_home.Clicked_Signin)
signin_button.place(x = 60, y = 100)

app_img = Image.open("Images/App name.png")
app_img = ImageTk.PhotoImage(app_img)
app = tkinter.Label(image = app_img, borderwidth = 0)
app.place(x = 262, y = 100)

login_img = Image.open("Images/Login.png")
login_img = ImageTk.PhotoImage(login_img)
login_button = tkinter.Button(image = login_img, borderwidth = 0, command = on_home.Clicked_Login)
login_button.place(x = 462, y = 100)

on_home.homebutton = tkinter.Button(text = "Go to home", command = on_home.HomePage)

# def track(event):
#     print(event.x, event.y)
# window.bind("<Motion>",track)


window.mainloop()



