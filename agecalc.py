from tkinter import *
import sv_ttk
from tkinter import ttk

w = Tk()
w.geometry('400x200')
sv_ttk.set_theme('light')
w.title('AgeCalc')

l = ttk.Label(w, text='Year of Birth')
l.pack(pady=10)

e = ttk.Entry(w)
e.pack(pady=10)

def submit():
    l1.config(text="Your Age: " + f'{2022-int(str(e.get()))}')
    
l1 = ttk.Label(w, text='')
l1.pack(pady=4)

b = ttk.Button(w, text='Submit', command=submit)
b.pack(pady=6)

w.mainloop()