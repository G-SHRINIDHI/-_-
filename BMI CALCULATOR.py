
#importing packages
from tkinter import*
import sys
import tkinter.messagebox
import tkinter as tk


    #creating the initial window
win=Tk()

    #giving a title
win.title("BMI")

win.geometry('900x800')

    #set window color
win.configure(bg='#FAEBD7')

    #to turn off min/max options
win.attributes('-toolwindow',True);

    #add a label
l2=Label(win,text = "         Calculate Your BMI",  
        font = ("Brush Script MT","40"),  
        background = "#FAEBD7",
        foreground = "#8B4513",width=20  )
l2.grid(column=0,row=0)


win.title("BMI CALCULATOR")
win.configure(bg='#FAEBD7')
tk.Label(win,text='       DETAILS',font=("Courier 22 bold"),bg='#FAEBD7').grid(row=1)
tk.Label(win,text='',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=2)
tk.Label(win,text='**Enter height(in cm)\n**Enter Weight(in Kg)',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=3)
tk.Label(win,text='',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=4)
tk.Label(win,text='HEIGHT    :',font=("Courier 15 bold"),bg='#FAEBD7').grid(row=5)
tk.Label(win,text='WEIGHT    :',font=("Courier 15 bold"),bg='#FAEBD7').grid(row=6)

e1=tk.Entry(win,font=("Courier 15 bold"))
e2=tk.Entry(win,font=("Courier 15 bold"))
            
e1.grid(row=5,column=1)
e2.grid(row=6,column=1)


def show_entry_fields():
   height=int(e1.get())
   weight=int(e2.get())
   h=float(height/100)
   BMI=float(weight/ (h**2))
   tk.Label(win,text='Your Body Mass Index is : %d' % BMI,font=("Courier 12 bold"),bg='#FAEBD7').grid(row=14,column=0)
   if BMI>0:
      if BMI<=16:
         tk.Label(win,text='You are severley underweight ',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=16)
      elif BMI<=18:
         tk.Label(win,text='You are underweight ',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=16)
      elif BMI<=25:
         tk.Label(win,text='You are Healthy ',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=16)
      elif BMI<=30:
         tk.Label(win,text='You are overweight ',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=16)
      else:
         tk.Label(win,text='You are severley overweight ',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=16)
   else:
         tk.Label(win,text='Please enter correct values',font=("Courier 12 bold"),bg='#FAEBD7').grid(row=16)

btn = Button(win, text = 'Quit',command = win.destroy)
btn.place(x=300,y=300)
btn1 = Button(win, text = 'Show',command = show_entry_fields)
btn1.place(x=400,y=300)
            
tk.mainloop()
win.mainloop()
