

#Python 3.4 (For 2.7 change tkinter to Tkinter)
    
from tkinter import * 
        
def show():
    p = password.get() #get password from entry
    print(p)
    passEntry.config(show = "")
        
    
app = Tk()   
password = StringVar() #Password variable
passEntry = Entry(app, textvariable=password, show='*')
submit = Button(app, text='Show Console',command=show)

passEntry.pack() 
submit.pack()      

app.mainloop() 