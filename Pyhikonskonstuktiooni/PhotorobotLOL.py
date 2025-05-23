# from tkinter.messagebox import showinfo
# import customtkinter as ctk
# from tkinter import simpledialog,Canvas
# from PIL import Image, ImageTk
# import pygame

# pildid = {}
# objektid = {}
# olemas = {}

# def toggle_osa(nimi, fail, x, y):
#     if olemas.get(nimi):
#         canvas.delete(objektid[nimi])
#         olemas[nimi] = False
#     else:
#         pil_img = Image.open(fail).convert("RGBA").resize((400, 400))
#         tk_img = ImageTk.PhotoImage(pil_img)
#         pildid[nimi] = tk_img
#         objektid[nimi]=canvas.create_image(x, y, image=tk_img)
#         olemas[nimi] = True

# def mängi_muusika():
#     pygame.mixer.music.play(loops=-1)

# def peata_muusika():
#     pygame.mixer.music.stop()

# def salvesta_nägu():
#     failinimi = simpledialog.askstring("Salvesta pilt", "Sisesta faili nimi (ilma laiendita:)")
#     if not failinimi:
#         return

#     lõpp_pilt = Image.new("RGBA", (400, 400), (255, 255, 255, 255))

#     for nimi in ["nägu", "otsmik", "silmad", "nina", "suu"]:
#         if olemas.get(nimi):
#             failitee = {
#                 "nägu": "alus.png",
#                 "otsmik": "aksesuar1.png",
#                 "silmad": "silmad.png",
#                 "nina": "nina.png",
#                 "suu": "suu.png"
#             }.get(nimi)
#             if failitee:
#                 osa = Image.open(failitee).convert("RGBA").resize((400, 400))
#                 lõpp_pilt.alpha_composite(osa)

#     lõpp_pilt.save(f"{failinimi}.png")
#     showinfo("Horaw! :D", f"faili nimi on {failinimi}.png")

# pygame.mixer.init()
# pygame.mixer.music.load("opening.mp3")
# # ctk.set_appearence_mode("Light")

# app= ctk.CTk()
# app.geometry("800x500")
# app.title("Neo")

# canvas= Canvas(app, width=400, height=400, bg="white")
# canvas.pack(side="right", padx=10, pady=10)

# toggle_osa("nägu", "alus.png", 200, 200)
# olemas["nägu"] = True

# frame = ctk.CTkFrame(app)
# frame.pack(side="left", padx=10, pady=10)
# seaded = {
#     "width": 150, "height": 40,
#     "font": ("Segoe UI Emoji", 32),
#     "fg_color": "white",
#     "corner_radius": 20
# }


# ctk.CTkButton(frame, text="Vali näoosad", **seaded).pack(pady=5)
# ctk.CTkButton(frame, text="Juuksed", command=lambda: toggle_osa("juuksed", "aksesuar1.png", 200, 200), **seaded).pack(pady=3)
# ctk.CTkButton(frame, text="Silmad", command=lambda: toggle_osa("silmad", "silmad.png", 200, 200), **seaded).pack(pady=3)
# ctk.CTkButton(frame, text="Nina", command=lambda: toggle_osa("nina", "nina.png", 200, 200), **seaded).pack(pady=3)
# ctk.CTkButton(frame, text="Suu", command=lambda: toggle_osa("suu", "suu.png", 200, 200), **seaded).pack(pady=3)
# ctk.CTkButton(frame, text="Loo nägu", command=lambda: salvesta_nägu(), **seaded).pack(pady=10)

# frame_mus = ctk.CTkFrame(frame)
# frame_mus.pack(padx=10, pady=10)
# ctk.CTkButton(frame_mus, text="Mängi muusikat", command=lambda: mängi_muusika(), **seaded).pack(side="left", pady=10)
# ctk.CTkButton(frame_mus, text="Peata muusikat", command=lambda: peata_muusika(), **seaded).pack(side="left", pady=10)

# app.mainloop()

from tkinter.messagebox import showinfo
import customtkinter as ctk
from tkinter import simpledialog, Canvas, ttk
from PIL import Image, ImageTk
import pygame
from tkinter.filedialog import asksaveasfilename

pildid = {}
objektid = {}
olemas = {}
valikud = {}

def toggle_osa(nimi, fail, x, y):
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi] = False
    else:
        try:
            pil_img = Image.open(fail).convert("RGBA").resize((400, 400))
            tk_img = ImageTk.PhotoImage(pil_img)
            pildid[nimi] = tk_img
            objektid[nimi] = canvas.create_image(x, y, image=tk_img)
            olemas[nimi] = True
        except FileNotFoundError:
            showinfo("Viga", f"Pilt puudub: {fail}")
        except Exception as e:
            showinfo("Tundmatu viga", f"Midagi läks valesti: {e}")

def toggle_valik(nimi, x, y):
    valik = valikud.get(nimi, 1)
    failinimi = f"{nimi}{valik}.png"
    toggle_osa(nimi, failinimi, x, y)

def muuda_valikut(nimi, valik):
    try:
        valikud[nimi] = int(valik)
        if olemas.get(nimi):
            toggle_valik(nimi, 200, 200)  # Remove
            toggle_valik(nimi, 200, 200)  # Add with new valik
    except Exception as e:
        showinfo("Viga", f"Ei saanud valikut muuta: {e}")

def mängi_muusika():
    pygame.mixer.music.play(loops=-1)

def peata_muusika():
    pygame.mixer.music.stop()

def salvesta_nägu():
    # Open Save As dialog, suggest PNG format
    failitee = asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG pildifailid", "*.png")],
        title="Salvesta pilt"
    )
    if not failitee:
        return  # User cancelled

    lõpp_pilt = Image.new("RGBA", (400, 400), (255, 255, 255, 255))
    osad = ["nägu", "otsmik", "juuksed", "silmad", "nina", "suu"]

    for nimi in osad:
        if nimi == "nägu":
            fail = "alus.png"
        else:
            if olemas.get(nimi):
                fail = f"{nimi}{valikud.get(nimi, 1)}.png"
            else:
                continue
        try:
            osa = Image.open(fail).convert("RGBA").resize((400, 400))
            lõpp_pilt.alpha_composite(osa)
        except FileNotFoundError:
            showinfo("Viga", f"Pilt puudub: {fail}")
            return
        except Exception as e:
            showinfo("Viga", f"Midagi läks valesti pildi laadimisel: {e}")
            return

    try:
        lõpp_pilt.save(failitee)
        showinfo("Horaw! :D", f"Fail salvestatud: {failitee}")
    except Exception as e:
        showinfo("Viga", f"Ei saanud faili salvestada: {e}")

pygame.mixer.init()
try:
    pygame.mixer.music.load("opening.mp3")
except Exception as e:
    showinfo("Viga", f"Muusika laadimine ebaõnnestus: {e}")

app = ctk.CTk()
app.geometry("800x500")
app.title("Neo")

canvas = Canvas(app, width=400, height=400, bg="white")
canvas.pack(side="right", padx=10, pady=10)

toggle_osa("nägu", "alus.png", 200, 200)
olemas["nägu"] = True

frame = ctk.CTkFrame(app)
frame.pack(side="left", padx=10, pady=10)

seaded = {
    "width": 150, "height": 40,
    "font": ("Segoe UI Emoji", 24),
    "fg_color": "white",
    "corner_radius": 20
}

ctk.CTkButton(frame, text="Vali näoosad", **seaded).pack(pady=5)

for nimi in ["juuksed", "silmad", "nina", "suu", "otsmik"]:
    rida = ctk.CTkFrame(frame)
    rida.pack(pady=3)
    ctk.CTkButton(rida, text=nimi.capitalize(), command=lambda n=nimi: toggle_valik(n, 200, 200), **seaded).pack(side="left")
    valik = ttk.Combobox(rida, values=[1, 2, 3, 4, 5], width=3)
    valik.current(0)
    valik.pack(side="left", padx=5)
    valik.bind("<<ComboboxSelected>>", lambda e, n=nimi, cb=valik: muuda_valikut(n, cb.get()))
    valikud[nimi] = 1

ctk.CTkButton(frame, text="Loo nägu", command=salvesta_nägu, **seaded).pack(pady=10)

frame_mus = ctk.CTkFrame(frame)
frame_mus.pack(padx=10, pady=10)
ctk.CTkButton(frame_mus, text="Mängi muusikat", command=mängi_muusika, **seaded).pack(side="left", pady=10)
ctk.CTkButton(frame_mus, text="Peata muusikat", command=peata_muusika, **seaded).pack(side="left", pady=10)

app.mainloop()
