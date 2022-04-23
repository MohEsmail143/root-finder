# from tkinter import *
#
# root = Tk()
# root.title("Numerical Solver")
# e = Entry(root, width=50, borderwidth=0.5)
# e.insert(0, "Enter Your Name:")
# e.pack()
#
#
# def my_click():
#     my_label = Label(root, text=e.get())
#     my_label.pack()
#
#
# myButton = Button(root, text="Click Me!", command=my_click)
# myButton.pack()
#
# root.mainloop()

from numpy import exp as exp

from numerical_methods import fixed_point

print(fixed_point(float(exp(-x) - x), float(exp(-x)), 0.005, 500))
