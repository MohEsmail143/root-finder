import time
from tkinter import *
from tkinter import messagebox

from numpy import *

import numerical_methods


# Opens results in new windows after pressing GO
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Iterations")

    # sets the geometry of toplevel
    newWindow.state('zoomed')

    # A Label widget to show in toplevel
    # Label(newWindow,text="This is a new window").pack()
    return newWindow


# Handling of bracketing methods and creates table iterations
def start_bracketing_method(method):
    f = lambda x: eval(f_x_entry.get().replace("^", "**"))
    xl = float(xl_entry.get())
    xu = float(xu_entry.get())
    es = float(es_entry.get())
    imax = int(imax_entry.get())
    if method == "Bisection":
        begin = time.time()
        res_ar = numerical_methods.bisection(xl, xu, f, es, imax)
        end = time.time()
    else:
        begin = time.time()
        res_ar = numerical_methods.false_position(xl, xu, f, es, imax)
        end = time.time()

    if res_ar == None:
        messagebox.showwarning("showwarning", "Warning: No root found")
        return
    nw = openNewWindow()
    font = ('Arial', 14, 'bold')
    xl_lbl = Label(nw, text="i", font=font)
    xl_lbl.grid(row=0, column=0)

    xl_lbl = Label(nw, text="xl", font=font)
    xl_lbl.grid(row=0, column=1)

    fxl_lbl = Label(nw, text="f(xl)", font=font)
    fxl_lbl.grid(row=0, column=2)

    xu_lbl = Label(nw, text="xu", font=font)
    xu_lbl.grid(row=0, column=3)

    fxu_lbl = Label(nw, text="f(xu)", font=font)
    fxu_lbl.grid(row=0, column=4)

    xr_lbl = Label(nw, text="xr", font=font)
    xr_lbl.grid(row=0, column=5)

    fxr_lbl = Label(nw, text="f(xr)", font=font)
    fxr_lbl.grid(row=0, column=6)

    ea_lbl = Label(nw, text="ea", font=font)
    ea_lbl.grid(row=0, column=7)

    # code for creating table

    i = 0
    j = 0
    for i in range(len(res_ar)):
        for j in range(len(res_ar[0])):
            e = Entry(nw, width=10, fg='blue', font=('Arial', 16, 'bold'))
            e.grid(row=i + 1, column=j)
            e.insert(END, res_ar[i][j])

    root_lbl = Label(nw, text=f"Root = {res_ar[i][5]}", font=font)
    root_lbl.grid(row=0, column=j + 1)
    time_lbl = Label(nw, text=f"Time = {str(end - begin)} s", font=font)
    time_lbl.grid(row=1, column=j + 1)


# Handling of the open methods and creates table iterations
def start_open_method(method):
    f = lambda x: eval(f_x_entry.get().replace("^", "**"))
    es = float(es_entry.get())
    imax = int(imax_entry.get())
    if method == "Fixed point":
        x0 = float(x0_entry.get())
        g = lambda x: eval(g_x_entry.get().replace("^", "**"))
        begin = time.time()
        res_ar = numerical_methods.fixed_point(x0, g, es, imax)
        end = time.time()
    elif method == "Newton-Raphson":
        f = f_x_entry.get().replace("^", "**")
        xi = float(xi_entry.get())
        begin = time.time()
        res_ar = numerical_methods.newton_raphson(xi, f, es, imax)
        end = time.time()
    elif method == "Secant":
        x_iminus1 = float(x_iminus1_entry.get())
        xi = float(xi_entry.get())
        begin = time.time()
        res_ar = numerical_methods.secant(x_iminus1, xi, f, es, imax)
        end = time.time()

        nw = openNewWindow()
        font = ('Arial', 14, 'bold')
        i_lbl = Label(nw, text="i", font=font)
        i_lbl.grid(row=0, column=0)

        x_iminus1_lbl = Label(nw, text="x i-1", font=font)
        x_iminus1_lbl.grid(row=0, column=1)

        xi_lbl = Label(nw, text="xi", font=font)
        xi_lbl.grid(row=0, column=2)

        xi_lbl = Label(nw, text="f(x i-1)", font=font)
        xi_lbl.grid(row=0, column=3)

        xi_lbl = Label(nw, text="f(xi)", font=font)
        xi_lbl.grid(row=0, column=4)

        xu_lbl = Label(nw, text="ea", font=font)
        xu_lbl.grid(row=0, column=5)

    if method == "Fixed point" or method == "Newton-Raphson":
        nw = openNewWindow()
        font = ('Arial', 14, 'bold')
        xl_lbl = Label(nw, text="i", font=font)
        xl_lbl.grid(row=0, column=0)

        xl_lbl = Label(nw, text="xi", font=font)
        xl_lbl.grid(row=0, column=1)

        fxl_lbl = Label(nw, text="x i+1", font=font)
        fxl_lbl.grid(row=0, column=2)

        xu_lbl = Label(nw, text="ea", font=font)
        xu_lbl.grid(row=0, column=3)

    # code for creating table
    i = 0
    j = 0
    for i in range(len(res_ar)):
        for j in range(len(res_ar[0])):
            e = Entry(nw, width=10, fg='blue', font=('Arial', 16, 'bold'))
            e.grid(row=i + 1, column=j)
            e.insert(END, res_ar[i][j])

    root_lbl = Label(nw, text=f"Root = {res_ar[i][2]}", font=font)
    root_lbl.grid(row=0, column=j + 1)
    time_lbl = Label(nw, text=f"Time = {str(end - begin)} s", font=font)
    time_lbl.grid(row=1, column=j + 1)


# Clicking Go button handling based on method choice
def go_func():
    # Replace '^' with '**' for Python interpreter

    if clicked.get() == "Bisection" or clicked.get() == "False-position":
        start_bracketing_method(clicked.get())
        # # print(xr)
        # return (xl_entry.get(), xu_entry.get(), f_x_entry.get(), clicked.get(), es_entry.get(), imax_entry.get())
    else:
        start_open_method(clicked.get())


# Drop down menu method selection handling. Shows method-specific parameters frame
def setMethodName(method_name):
    # print(method_name)
    global xl_entry, xu_entry, g_x_entry, xi_entry, x0_entry, x_iminus1_entry
    clicked.set(method_name)
    for widgets in method_frame.winfo_children():
        widgets.destroy()
    # method_frame.destroy()
    # method_frame.
    # method_frame = LabelFrame(root, text="Method-specific Parameters")
    # method_frame.grid_remove()
    # method_frame.grid(row=4, column=0, rowspan=2, columnspan=2, padx=5, pady=5)

    if method_name == "Bisection" or method_name == "False-position":
        xl_lbl = Label(method_frame, text="xl = ")
        xl_entry = Entry(method_frame, width=20)
        xu_lbl = Label(method_frame, text="xu = ")
        xu_entry = Entry(method_frame, width=20)

        xl_lbl.grid(row=0, column=0, padx=5, pady=5)
        xl_entry.grid(row=0, column=1, padx=5, pady=5)
        xu_lbl.grid(row=1, column=0, padx=5, pady=5)
        xu_entry.grid(row=1, column=1, padx=5, pady=5)

    elif clicked.get() == "Fixed point":

        g_x_lbl = Label(method_frame, text="g(x) = ")
        g_x_entry = Entry(method_frame, width=20)
        x0_lbl = Label(method_frame, text="x0 = ")
        x0_entry = Entry(method_frame, width=20)

        g_x_lbl.grid(row=0, column=0, padx=5, pady=5)
        g_x_entry.grid(row=0, column=1, padx=5, pady=5)
        x0_lbl.grid(row=1, column=0, padx=5, pady=5)
        x0_entry.grid(row=1, column=1, padx=5, pady=5)
    elif clicked.get() == "Newton-Raphson":
        xi_lbl = Label(method_frame, text="xi = ")
        xi_entry = Entry(method_frame, width=20)
        xi_lbl.grid(row=0, column=0, padx=5, pady=5)
        xi_entry.grid(row=0, column=1, padx=5, pady=5)
    elif clicked.get() == "Secant":
        x_iminus1_lbl = Label(method_frame, text="x i-1 = ")
        x_iminus1_entry = Entry(method_frame, width=20)
        xi_lbl = Label(method_frame, text="xi = ")
        xi_entry = Entry(method_frame, width=20)
        x_iminus1_lbl.grid(row=0, column=0, padx=5, pady=5)
        x_iminus1_entry.grid(row=0, column=1, padx=5, pady=5)
        xi_lbl.grid(row=1, column=0, padx=5, pady=5)
        xi_entry.grid(row=1, column=1, padx=5, pady=5)


# Take input from txt file
def file_opener():
    res = ''
    from tkinter import filedialog
    input = filedialog.askopenfile(initialdir="../")
    for i in input:
        res += i
    # x = len(equation.get())
    f_x_entry.delete(0, END)
    f_x_entry.insert(0, res)


if __name__ == '__main__':
    root = Tk()
    root.title("Numerical Solver")
    root.geometry("480x360")
    root.resizable(False, False)
    p1 = PhotoImage(file='icon.png')
    root.iconphoto(False, p1)

    # Labels
    f_x_lbl = Label(root, text="f(x) = ")
    method_lbl = Label(root, text="Method")
    es_lbl = Label(root, text="es")
    imax_lbl = Label(root, text="Max Iterations")

    # Text boxes
    f_x_entry = Entry(root, width=35, borderwidth=3)
    es_entry = Entry(root, width=20)
    es_entry.insert(0, "0.00001")

    imax_entry = Entry(root, width=20)
    imax_entry.insert(0, "50")

    # Drop-down Menu
    options = ["Bisection", "False-position", "Fixed point", "Newton-Raphson", "Secant"]
    clicked = StringVar()
    clicked.set("")
    methods_dropdown = OptionMenu(root, clicked, *options, command=setMethodName)
    methods_dropdown.config(width=20)

    # Buttons
    reset_btn = Button(root, text="Reset", width=20)
    clear_results_btn = Button(root, text="Clear Results", width=20)
    single_step_btn = Button(root, text="Single-step", width=20)
    go_btn = Button(root, text="Go", width=20, command=go_func)
    f_x_entry_btn = Button(root, text="Browse File", command=file_opener)

    # Frames
    method_frame = LabelFrame(root, text="Method-specific Parameters")

    # Root Grid
    f_x_lbl.grid(row=0, column=0, padx=5, pady=5)
    f_x_entry.grid(row=0, column=1, padx=5, pady=5)
    # equation.grid(row=0, column=3, padx=5, pady=5)
    f_x_entry_btn.grid(row=0, column=2, padx=5, pady=5)
    method_frame.grid(row=4, column=0, rowspan=2, columnspan=2, padx=5, pady=5)
    method_lbl.grid(row=1, column=0, padx=5, pady=5)
    methods_dropdown.grid(row=1, column=1, padx=5, pady=5)
    es_lbl.grid(row=2, column=0, padx=5, pady=5)
    es_entry.grid(row=2, column=1, padx=5, pady=5)
    imax_lbl.grid(row=3, column=0, padx=5, pady=5)
    imax_entry.grid(row=3, column=1, padx=5, pady=5)
    reset_btn.grid(row=7, column=0, padx=5, pady=5)
    clear_results_btn.grid(row=7, column=1, padx=5, pady=5)
    single_step_btn.grid(row=8, column=0, padx=5, pady=5)
    go_btn.grid(row=8, column=1, padx=5, pady=5)

    root.mainloop()
