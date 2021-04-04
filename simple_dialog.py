from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
root= Tk()

def func():
    answer = messagebox.askyesno(message="You sure?")
    my_nick = simpledialog.askstring("замечание", "введите Ваш ник ")
    lbl.config(text=my_nick)

btn = Button(root, text= 'push me', command=func)
btn.pack()

lbl=Label(root, text='Name')
lbl.pack()


root.mainloop()