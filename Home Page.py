import tkinter
from tkinter.constants import END
from PIL import Image, ImageTk
import json
import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# choose what to use, like window or anything and where to use
window = tkinter.Tk()
window.minsize(height = 500, width = 700)


class Home:
    def CreatingAccount(self):
        f=open("logindetails.json","r+")
        contents = f.read()
        js = json.loads(contents)
        js.append({'username': self.username, 'password': self.password})
        f.seek(0)       
        f.write(json.dumps(js, indent=2))
        f.truncate()
        f.close()
    
    def CheckingForAccount(self):
        f = open("logindetails.json","r+")
        contents = f.read()
        js = json.loads(contents)
        self.email = True
        for i in range(len(js)):
            if js[i]['username'] == self.username:
                if js[i]['password'] == self.password:
                    print("Login Successful")
                    self.email = True
                    break
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
        self.next.place(x = 550, y = 225)
        
    def Clicked_Login(self):
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
        self.next.place(x = 350, y = 225)

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

# def Motion(event):
#     print(event.x, event.y)

# window.bind("<Motion>",Motion)

window.mainloop()