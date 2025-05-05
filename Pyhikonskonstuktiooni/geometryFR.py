from tkinter import *
from tkinter.font import *

def ColorAndCalcolusGO():
    a = sisetus
    b = sisetus2
    c = sisetus3

    if a is None:
        sisetus.config(bg="red")
    else:
        sisetus.config(bg="lightblue")

    if b is None:
        sisetus2.config(bg="red")
    else:
        sisetus2.config(bg="lightblue")

    if c is None:
        sisetus3.config(bg="red")
    else:
        sisetus3.config(bg="lightblue")

    D=b**2-4*a*c
    if D>0:
        pealkiri2.config(text=f"D = {D}, seal on 2", bg="yellow", fg="black")
    elif D == 0:
        pealkiri2.config(text=f"D = {D}, seal on 1", bg="yellow", fg="black")
    elif D<0:
        pealkiri2.config(text=f"D = {D}, seal pole", bg="yellow", fg="black")


aken=Tk()
# aken.wm_attributes('-transparentcolor','gray')
aken.title("matikaFORrealMEN")
aken.geometry("600x200")
aken.configure(bg="white")
#attributes('-alpha',0.5)
aken.resizable(width=False, height=False)
aken.iconbitmap("Clover_overworld.ico")
pealkiri = Label(aken, text="Ruutvõrrandi lahendamine", bg ="lightblue", font=("Arial", 16, BOLD), fg="green")
meaning = Label(aken, text="x²+", bg ="white", font=("Arial", 16), fg="green")
meaning2 = Label(aken, text="x+", bg ="white", font=("Arial", 16), fg="green")
meaning3 = Label(aken, text="=0", bg ="white", font=("Arial", 16), fg="green")
nupp=Button(aken, text="Otsusta", bg="green", font=("Arial", 12), fg="black", relief= SUNKEN, command=ColorAndCalcolusGO)
pealkiri2=Label(aken, text="Otsustamine", bg ="yellow", font=("Arial", 12, BOLD), fg="black", width=20, height=5)
sisetus=Entry(aken, bg="lightblue", font=("Arial", 12), fg="black", width=3)
sisetus2=Entry(aken, bg="lightblue", font=("Arial", 12), fg="black", width=3)
sisetus3=Entry(aken, bg="lightblue", font=("Arial", 12), fg="black", width=3)
# #SUNKEN, RAISED, GROOVE, and RIDGE

pealkiri.place(x=180, y=10)
sisetus.place(x=20, y=50)
meaning.place(x=70, y=50)
sisetus2.place(x=120, y=50)
meaning2.place(x=150, y=50)
sisetus3.place(x=180, y=50)
meaning3.place(x=210, y=50)
nupp.place(x=250, y=50)
pealkiri2.place(x=250, y=100)



# nupp=Button(aken, text="Press me if ur silly :3 (meow, mrrrr)", bg="yellow", font=("Arial", 12), fg="green", relief= SUNKEN, command=vajatatud)
# #SUNKEN, RAISED, GROOVE, and RIDGE

# nupp.bind("<Button-3>", vajatatudPK)
# sisetus=Entry(aken, bg="white", font=("Arial", 12), fg="black")
# sisetus.insert(0, "Sisesta midagi siia") #END
# sisetus.bind("<FocusIn>", tuhista)

# pealkiri.pack(pady=20)
# sisetus.pack(pady=20)
# nupp.pack(pady=20)




aken.mainloop()
