from tkinter import *
from tkinter.font import *

k=0

def vajatatud():
    global k
    k+=1
    pealkiri.config(text=f"""Now you are silly!
    your silinnes level = {k}!""", bg="green", fg="blue")
    nupp.config(text="Continiue pressing >:3 , mrrr!", bg="orange", fg="blue")

def vajatatudPK(event):
    global k
    k-=1
    pealkiri.config(text=f"""Now you are silly!
    your silinnes level = {k}!""", bg="black", fg="white")
    nupp.config(text="Continiue pressing >:3 , meow!", bg="red", fg="white")

def tuhista(event):
    sisetus.delete(0, END)

aken=Tk()
aken.title("Teema 8")
aken.geometry("400x400")
aken.configure(bg="lightblue")
aken.resizable(width=False, height=False)
aken.iconbitmap("Clover_overworld.ico")
pealkiri = Label(aken, text="lmao im a funny text", bg ="blue", font=("Arial", 16, BOLD), fg="green")

nupp=Button(aken, text="Press me if ur silly :3 (meow, mrrrr)", bg="yellow", font=("Arial", 12), fg="green", relief= SUNKEN, command=vajatatud)
#SUNKEN, RAISED, GROOVE, and RIDGE

nupp.bind("<Button-3>", vajatatudPK)
sisetus=Entry(aken, bg="white", font=("Arial", 12), fg="black")
sisetus.insert(0, "Sisesta midagi siia") #END
sisetus.bind("<FocusIn>", tuhista)

pealkiri.pack(pady=20)
sisetus.pack(pady=20)
nupp.pack(pady=20)




aken.mainloop()