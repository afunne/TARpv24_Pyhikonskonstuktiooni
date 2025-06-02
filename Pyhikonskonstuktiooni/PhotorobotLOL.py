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
from tkinter import simpledialog, Canvas
from tkinter.filedialog import asksaveasfilename
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk
import pygame

pildid = {}
objektid = {}
olemas = {}
valikud = {}
alus_index = 1

valiku_nimed = {
    "aksesuar": ["Peapael", "Müts", "Prillid", "Kõrvarõngad", "Kiiver"],
    "silmad": ["Suured silmad", "Vihased silmad", "Unised silmad", "Naerused silmad", "Kassisilmsed"],
    "nina": ["Väike nina", "Suur nina", "Konksnina", "Nuppnina", "Sirge nina"],
    "suu": ["Naeratus", "Huuled koos", "Üllatunud", "Kurb", "Suu lahti"]
}

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
        except Exception as e:
            showinfo("Viga", f"Ei saanud faili laadida: {fail}\n{e}")

def toggle_valik(nimi, x, y):
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi] = False
    else:
        fail = f"{nimi}{valikud.get(nimi, 1)}.png"
        toggle_osa(nimi, fail, x, y)

def muuda_valikut(nimi, valik):
    try:
        valikud[nimi] = int(valik)
        if olemas.get(nimi):
            canvas.delete(objektid[nimi])
            olemas[nimi] = False
            toggle_valik(nimi, 200, 200)
    except Exception as e:
        showinfo("Viga", f"Ei saanud valikut muuta: {e}")

def mängi_muusika():
    pygame.mixer.music.play(loops=-1)

def peata_muusika():
    pygame.mixer.music.stop()

def vaheta_alus():
    global alus_index
    if olemas.get("nägu"):
        canvas.delete(objektid["nägu"])
        olemas["nägu"] = False

    alus_index = 2 if alus_index == 1 else 1
    uus_fail = f"alus{'' if alus_index == 1 else '2'}.png"

    try:
        toggle_osa("nägu", uus_fail, 200, 200)
        olemas["nägu"] = True
    except Exception as e:
        showinfo("Viga", f"Ei saanud alusfaili laadida: {uus_fail}\n{e}")

def salvesta_nägu(): # a reminder to myself to show an example here! :3
    global alus_index
    failitee = asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG pildifailid", "*.png")],
        title="Salvesta pilt"
    )
    if not failitee:
        return

    lõpp_pilt = Image.new("RGBA", (400, 400), (0, 0, 0, 0))
    osad = ["nägu", "otsmik", "aksesuar", "silmad", "nina", "suu"]

    for nimi in osad:
        if nimi == "nägu":
            fail = f"alus{'' if alus_index == 1 else '2'}.png"
        elif olemas.get(nimi):
            fail = f"{nimi}{valikud.get(nimi, 1)}.png"
        else:
            continue

        try:
            osa = Image.open(fail).convert("RGBA").resize((400, 400))
            lõpp_pilt = Image.alpha_composite(lõpp_pilt, osa)
        except FileNotFoundError:
            showinfo("Viga", f"Pilt puudub: {fail}")
            return
        except Exception as e:
            showinfo("Viga", f"Pildi lisamine ebaõnnestus: {e}")
            return

    try:
        lõpp_pilt.save(failitee)
        showinfo("Horaw! :D", f"Fail salvestatud: {failitee}")
    except Exception as e:
        showinfo("Viga", f"Ei saanud faili salvestada: {e}")


    # open and stack the image
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

ctk.CTkButton(frame, text="Vali näoosad", text_color="black", **seaded).pack(pady=5)

for nimi in ["aksesuar", "silmad", "nina", "suu"]:
    rida = ctk.CTkFrame(frame)
    rida.pack(pady=3)

    ctk.CTkButton(rida, text=nimi.capitalize(), text_color="black",
                  command=lambda n=nimi: toggle_valik(n, 200, 200), **seaded).pack(side="left")

    nimed = valiku_nimed[nimi]
    valik = ttk.Combobox(rida, values=nimed, width=18)
    valik.current(0)
    valik.pack(side="left", padx=5)

    def create_bind_callback(nimi, combobox, nimed):
        return lambda e: muuda_valikut(nimi, str(nimed.index(combobox.get()) + 1))

    valik.bind("<<ComboboxSelected>>", create_bind_callback(nimi, valik, nimed))
    valikud[nimi] = 1

ctk.CTkButton(frame, text="Loo nägu", text_color="black", command=salvesta_nägu, **seaded).pack(pady=10)
ctk.CTkButton(frame, text="Vaheta teemat", text_color="black", command=vaheta_alus, **seaded).pack(pady=5)

frame_mus = ctk.CTkFrame(frame)
frame_mus.pack(padx=10, pady=10)
ctk.CTkButton(frame_mus, text="Mängi muusikat", text_color="black", command=mängi_muusika, **seaded).pack(side="left", pady=10)
ctk.CTkButton(frame_mus, text="Peata muusikat", text_color="black", command=peata_muusika, **seaded).pack(side="left", pady=10)

app.mainloop()

