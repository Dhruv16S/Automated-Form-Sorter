# import tkinter
# from tkinter.constants import BOTTOM, COMMAND, LEFT, RIGHT, TOP
# window = tkinter.Tk()
# window.minsize(height = 500, width = 500)
# def Where1():
#     MECH.destroy()
#     MECH1 = tkinter.Label(text = "Welcome to Mechanical Department").pack(side = BOTTOM)

# def Where2():
#     CSE.destroy()
#     CSE1 = tkinter.Label(text = "Welcome to CSE Department").pack(side = LEFT)

# def Where3():
#     ECE.destroy()
#     ECE1 = tkinter.Label(text = "Welcome to ECE Department").pack(side = TOP)

# def Where4():
#     IT.destroy()
#     IT1 = tkinter.Label(text = "Welcome to IT Department").pack(side = RIGHT)

# heading = tkinter.Label(text = "Branches in CBIT").pack()
# CSE = tkinter.Button(text = "CSE", background = "Blue", command = Where2)
# CSE.pack(side = LEFT)
# ECE = tkinter.Button(text = "ECE", background = "Red", command = Where3)
# ECE.pack(side = TOP)
# IT = tkinter.Button(text = "IT", background = "Yellow", command = Where4)
# IT.pack(side = RIGHT)
# MECH = tkinter.Button(text = "MECH", background = "Green", command = Where1)
# MECH.pack(side = BOTTOM)

# colours = ["red", "blue", "orange", "magenta"]
# for colour in colours:
#     tkinter.Label(text = colour, width = 15, fg = colour).grid(row = colours.index(colour), column = 0)
#     tkinter.Entry(width = 10, background = colour).grid(row = colours.index(colour), column = 1)
# window.bind("<Motion>", lambda event : print(event.x, event.y))
# # window.mainloop()
import tkinter as tk


    

root = tk.Tk()

text = tk.Text(root)
img = tk.PhotoImage(file = "App name.gif")
text.pack(padx = 20, pady = 20)
text.image_create(tk.END, image = img) # Example 1




root.mainloop()