from tkinter import *
from tkinter.font import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

def ColorAndCalcolusGO():
    try:
        a = float(sisetus.get())
        sisetus.config(bg="lightblue")
    except:
        sisetus.config(bg="red")
        a = None

    try:
        b = float(sisetus2.get())
        sisetus2.config(bg="lightblue")
    except:
        sisetus2.config(bg="red")
        b = None

    try:
        c = float(sisetus3.get())
        sisetus3.config(bg="lightblue")
    except:
        sisetus3.config(bg="red")
        c = None

    if a is None or b is None or c is None:
        pealkiri2.config(text=">:O", bg="red")
        return

    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        result = f"x₁ = {x1:.2f}\nx₂ = {x2:.2f} \nseol on kaks juurt"
    elif D == 0:
        x = -b / (2 * a)
        result = f"x = {x:.2f}\nseol on uks juur"
    elif D < 0:
        result = "(D < 0) \njuurt pole"

    pealkiri2.config(text=f"D = {b}² - 4*{a}*{c} = {D}\n" + result, bg="yellow", fg="black")




def itsrainingtacos():
    try:
        a = float(sisetus.get())
        b = float(sisetus2.get())
        c = float(sisetus3.get())
    except:
        pealkiri2.config(text=">:[", bg="red")
        return

    if a == 0:
        pealkiri2.config(text="See ei ole kvadraatiline võrrand (a ≠ 0).", bg="red")
        return

    x_ver = -b / (2 * a)
    y_ver= a * x_ver ** 2 + b * x_ver + c

    x = np.linspace(x_ver - 10, x_ver + 10, 500)
    y = a * x ** 2 + b * x + c

    D = b**2 - 4 * a * c
    roots = []

    if D > 0:
        root1 = (-b + sqrt(D)) / (2 * a)
        root2 = (-b - sqrt(D)) / (2 * a)
        roots = [root1, root2]
    elif D == 0:
        root = -b / (2 * a)
        roots = [root]

    plt.figure()
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}', color='blue')  # smooth curve
    plt.scatter(x_ver, y_ver, color='green', zorder=5)

    for r in roots:
        plt.scatter(r, 0, color='red', label=f'juht: x={r:.2f}', zorder=5)

    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.title("ruutiline võrrand")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

# def show_graph():
#     try:
#         a = float(sisetus.get())
#         b = float(sisetus2.get())
#         c = float(sisetus3.get())
#     except:
#         pealkiri2.config(text="Sisestage õiged väärtused graafiku joonistamiseks!", bg="red")
#         return

#     x = np.linspace(-10, 10, 400)
#     y = a * x ** 2 + b * x + c

#     plt.figure()
#     plt.plot(x, y, linestyle='-', marker='o', color='blue',
#          markersize=8, markerfacecolor='lightblue', label="Tõusev joon")
#     plt.title("Ruutvõrrandi graafik")
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.grid(True)
#     plt.legend()
#     plt.show()


aken = Tk()
aken.title("MatimatikaFORrealMEN")
aken.geometry("600x300")
aken.configure(bg="white")
aken.iconbitmap("Clover_overworld.ico")
aken.resizable(False, False)


pealkiri = Label(aken, text="Ruutvõrrandi graafik", bg="lightblue", font=("Arial", 16, BOLD), fg="green")
meaning = Label(aken, text="x² +", bg="white", font=("Arial", 16), fg="green")
meaning2 = Label(aken, text="x +", bg="white", font=("Arial", 16), fg="green")
meaning3 = Label(aken, text="= 0", bg="white", font=("Arial", 16), fg="green")

nupp = Button(aken, text="Lahendada", bg="green", font=("Arial", 12), fg="black", command=ColorAndCalcolusGO)
graph = Button(aken, text="graafik", bg="green", font=("Arial", 12), fg="black", command=itsrainingtacos)

pealkiri2 = Label(aken, text=":3", bg="lightyellow", font=("Arial", 12), fg="black", width=40, height=6)

sisetus = Entry(aken, bg="lightblue", font=("Arial", 12), fg="black", width=5)
sisetus2 = Entry(aken, bg="lightblue", font=("Arial", 12), fg="black", width=5)
sisetus3 = Entry(aken, bg="lightblue", font=("Arial", 12), fg="black", width=5)


pealkiri.place(x=160, y=10)
sisetus.place(x=120, y=60)
meaning.place(x=170, y=60)
sisetus2.place(x=210, y=60)
meaning2.place(x=260, y=60)
sisetus3.place(x=300, y=60)
meaning3.place(x=350, y=60)
nupp.place(x=400, y=60)
graph.place(x=490, y=60)
pealkiri2.place(x=120, y=120)

aken.mainloop()
