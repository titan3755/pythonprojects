import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import time as t

#Main
root = Tk()
root.title('Area and Volume Calculator')
root.geometry('1000x600')
root.resizable(False, False)

#Functions and Windows




#Widgets
main_title = Label(root)
main_info = Text(root)
rectangular_triangular_calculations = Button(root)
pyramid_cylinder_calculations = Button(root)
circular_spherical_calculations = Button(root)
conical_calculations = Button(root)


#Configure
main_title.config(text='Geometric Calculator', font=('Helvetica', 28, 'italic'), bg='darkred', fg='white', padx=300, pady=12, border=5)
main_info.config(font=('Helvetica', 19), bg='#ff6a00', fg='black', width=50, height=4)
main_info.insert(1.0, 'Welcome to Geometrical calculator! Here you can do all kinds of volume and area calculations including cone, circle, triangle, pyramid, sphere, cylinder etc objects. Click one of the buttons below to open the corresponding calculator.')
main_info.config(state='disabled')

#Display
main_title.pack(anchor=CENTER)
main_info.pack(anchor=CENTER)


#APP LOOP
root.mainloop()



