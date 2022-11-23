from tkinter import *
from dark_title_bar import *

w = Tk()
w.geometry('400x200')
w.title('AgeCalc')
w.configure(bg='#1c1c1c')
w.resizable(False,False)
w.iconbitmap('icon.ico')
dark_title_bar(w)

l = Label(w, text='Year of Birth', background='#1c1c1c', foreground='white')
l.pack(pady=10)

e = Entry(w, background='#242424', foreground='white')
e.pack(pady=10)

def submit():
    l1.config(text="Your Age: " + f'{2022-int(str(e.get()))}')
    
l1 = Label(w, text='', background='#1c1c1c', foreground='white')
l1.pack(pady=4)

b = Button(w, text='Submit', command=submit, background='#242424', foreground='white')
b.pack(pady=6)

w.mainloop()