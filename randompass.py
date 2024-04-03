#importing packages
import random
from tkinter import *
import tkinter as tk
from tkinter.ttk import *


    #creating the initial window
win=Tk()
var = IntVar()
var1 = IntVar()


    #giving a title
win.title("Random Password Generator")

win.geometry('900x800')

    #set window color
win.configure(bg='#FAEBD7')

    #to turn off min/max options
win.attributes('-toolwindow',True);

    #add a label
l2=Label(win,text = "Create a Random password",  
        font = ("Brush Script MT","40"),  
        background = "#FAEBD7",
        foreground = "#8B4513",width=25  )
l2.grid(column=0,row=0)

#giving heading and details

win.title("Random Password Generator")
win.configure(bg='#FAEBD7')
tk.Label(win,text='  DETAILS',font=("Courier 22 bold"),bg='#FAEBD7').grid(row=1)
tk.Label(win,text='',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=2)
tk.Label(win,text='**Choose length and level \n to set a random password',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=3,column=0)
tk.Label(win,text='',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=4)


tk.Label(win,text='Length',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=5,column=0)
 
#creating radio button for strength of password
radio_low = Radiobutton(win, text="low", variable=var, value=1)
radio_low.grid(row=5, column=2, sticky='E')
radio_middle = Radiobutton(win, text="medium", variable=var, value=2)
radio_middle.grid(row=5, column=3, sticky='E')
radio_strong = Radiobutton(win, text="high", variable=var, value=3)
radio_strong.grid(row=5, column=4, sticky='E')
combo = Combobox(win, textvariable=var1)
 
# Combo Box for length of your password
combo['values'] = ("select a length",8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(row=5,column=1)

#fuction to generate password
def generate():
   length = var1.get()
   
   entry=Entry(win)
   entry.delete(0, END)
    
   lower = "abcdefghijklmnopqrstuvwxyz"
   upper = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
   digits="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()"
   
   characterList =""
   
   # if strength selected is low
   if var.get() == 1:
      for i in range(0, length):
         characterList=characterList+ random.choice(lower)
      return characterList
 
    # if strength selected is medium
   elif var.get() == 2:
      for i in range(0, length):
         characterList=characterList+ random.choice(upper)
      return characterList
      
    # if strength selected is strong
   elif var.get() == 3:
      for i in range(0, length):
         characterList=characterList+ random.choice(digits)
      return characterList
      
   else:
        tk.Label(win,text='please choose option',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=7,column=0)

def show_entry_fields():
   password1 = generate()
   tk.Label(win,text="The random password is : %s" % password1,font=("Courier 12 bold"),bg='#FAEBD7').grid(row=8,column=0)

btn = Button(win, text = 'Quit',command = win.destroy)
btn.place(x=300,y=300)
btn1 = Button(win, text = 'Show',command = show_entry_fields)
btn1.place(x=400,y=300)
            
tk.mainloop()
win.mainloop()



