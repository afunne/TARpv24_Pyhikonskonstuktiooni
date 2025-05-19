from tkinter.messagebox import showinfo
import customtkinter as ctk
from tkinter import simpledialog,Canvas
from PIL import Image, ImageTk
import pygame

pildid = {}
objektid = {}
olemas = {}

def toggle_osa(nimi, fail, x, y):
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi] = False
    else:
        pil_img = Image.open(fail).convert("RGBA").resize((400, 400))
        tk_img = ImageTk.PhotoImage(pil_img)
        pildid[nimi] = tk_img
        objektid[nimi]=canvas.create_image(x, y, image=tk_img)
        olemas[nimi] = True

def mängi_muusika():
    pygame.mixer.music.play(loops=-1)

def peata_muusika():
    pygame.mixer.music.stop()

def salvesta_nägu():
    failinimi = simpledialog.askstring("Salvesta pilt", "Sisesta faili nimi (ilma laiendita:)")
    if not failinimi:
        return

    lõpp_pilt = Image.new("RGBA", (400, 400), (255, 255, 255, 255))

    for nimi in ["nägu", "otsmik", "silmad", "nina", "suu"]:
        if olemas.get(nimi):
            failitee = {
                "nägu": "alus.png",
                "otsmik": "aksesuar1.png",
                "silmad": "silmad.png",
                "nina": "nina.png",
                "suu": "suu.png"
            }.get(nimi)
            if failitee:
                osa = Image.open(failitee).convert("RGBA").resize((400, 400))
                lõpp_pilt.alpha_composite(osa)

    lõpp_pilt.save(f"{failinimi}.png")
    showinfo("Horaw! :D", f"faili nimi on {failinimi}.png")

pygame.mixer.init()
pygame.mixer.music.load("opening.mp3")
# ctk.set_appearence_mode("Light")

app= ctk.CTk()
app.geometry("800x500")
app.title("Neo")

canvas= Canvas(app, width=400, height=400, bg="white")
canvas.pack(side="right", padx=10, pady=10)

toggle_osa("nägu", "alus.png", 200, 200)
olemas["nägu"] = True

frame = ctk.CTkFrame(app)
frame.pack(side="left", padx=10, pady=10)
seaded = {
    "width": 150, "height": 40,
    "font": ("Segoe UI Emoji", 32),
    "fg_color": "white",
    "corner_radius": 20
}


ctk.CTkButton(frame, text="Vali näoosad", **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Juuksed", command=lambda: toggle_osa("juuksed", "aksesuar1.png", 200, 200), **seaded).pack(pady=3)
ctk.CTkButton(frame, text="Silmad", command=lambda: toggle_osa("silmad", "silmad.png", 200, 200), **seaded).pack(pady=3)
ctk.CTkButton(frame, text="Nina", command=lambda: toggle_osa("nina", "nina.png", 200, 200), **seaded).pack(pady=3)
ctk.CTkButton(frame, text="Suu", command=lambda: toggle_osa("suu", "suu.png", 200, 200), **seaded).pack(pady=3)
ctk.CTkButton(frame, text="Loo nägu", command=lambda: salvesta_nägu(), **seaded).pack(pady=10)

frame_mus = ctk.CTkFrame(frame)
frame_mus.pack(padx=10, pady=10)
ctk.CTkButton(frame_mus, text="Mängi muusikat", command=lambda: mängi_muusika(), **seaded).pack(side="left", pady=10)
ctk.CTkButton(frame_mus, text="Peata muusikat", command=lambda: peata_muusika(), **seaded).pack(side="left", pady=10)

app.mainloop()