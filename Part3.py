from tkinter import *
from tkinter import filedialog
root=Tk()
my_label=Label(text="Links",font=18)
my_label.place(y=100,x=200)
def open_file():
    root.filename=filedialog.askopenfilename(initialdir='c:/',title="Select a file",filetypes=(("png files",".png"),("all files",".*")))
    mystr=StringVar()
    mystr.set(root.filename)
    entry=Entry(textvariable=mystr,state=DISABLED).place(y=50,x=300)
def save_links():
    cmd_text=cmd.get()
    print(cmd_text)
button_open_file=Button(text="Reference_file",command=open_file,bg='red')
button_open_file.place(y=50,x=200)
cmd=Entry(width=20)
cmd.place(y=100,x=300)
button_links=Button(text='Done',command=save_links)
button_links.place(y=100,x=500)
root.mainloop()