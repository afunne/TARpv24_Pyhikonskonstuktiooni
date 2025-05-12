# from tkinter import *
# from PIL import Image, ImageTk
# import pygame
# import random

# # Initialize pygame mixer
# pygame.mixer.init()

# # Choose a random audio file
# file = ['opening.mp3', 'Hip_Hop.mp3']
# random_ost = random.choice(file)

# # Load and loop the music
# def play_music():
#     pygame.mixer.music.load(random_ost)
#     pygame.mixer.music.play(loops=-1)  # loops=-1 means loop forever

# # Create the Tkinter window
# win = Tk()
# win.title("EmailSender")
# win.geometry("700x350")

# # Load and resize image
# image = Image.open('funnememe.png')
# img = image.resize((150, 150))
# my_img = ImageTk.PhotoImage(img)

# # Show image in the GUI
# label = Label(win, image=my_img)
# label.place(x=490, y=60)

# # Start playing music
# play_music()

# # Start the GUI loop
# win.mainloop()

# # Stop the music after the window closes
# pygame.mixer.music.stop()


# from tkinter import *
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk
# import pygame
# import smtplib
# from email.message import EmailMessage
# import random
# import os

# # --- Email Configuration ---
# GMAIL_USER = "tahmazovhussejn@gmail.com"
# GMAIL_APP_PASSWORD = "oxisfyxphjyfmdwi"  # Replace with your Gmail App Password

# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587

# # --- Music Setup ---
# pygame.mixer.init()
# songs = ['opening.mp3', 'Hip_Hop.mp3']
# pygame.mixer.music.load(random.choice(songs))
# pygame.mixer.music.play(-1)  # Loop forever

# # --- Email sending function ---
# def send_email():
#     to_email = to_entry.get().strip()
#     subject = subject_entry.get().strip()
#     attachment_path = attach_entry.get().strip()
#     body = message_text.get("1.0", END).strip()

#     if not to_email or not subject or not body:
#         messagebox.showwarning("Tühjad väljad", "Palun täida kõik kohustuslikud väljad.")
#         return

#     msg = EmailMessage()
#     msg["From"] = GMAIL_USER
#     msg["To"] = to_email
#     msg["Subject"] = subject
#     msg.set_content(body)

#     if attachment_path and os.path.exists(attachment_path):
#         with open(attachment_path, "rb") as f:
#             file_data = f.read()
#             file_name = os.path.basename(attachment_path)
#         msg.add_attachment(file_data, maintype="image", subtype="png", filename=file_name)

#     try:
#         with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#             server.starttls()
#             server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
#             server.send_message(msg)
#         messagebox.showinfo("Edu!", "E-kiri saadetud edukalt!")
#     except Exception as e:
#         messagebox.showerror("Viga", f"Ei saanud kirja saata:\n{e}")

# # it is for putting images, I wonder if I could send gifs...
# # I might actually add it tbh
# def attach_image():
#     file_path = filedialog.askopenfilename(title="Vali pilt", filetypes=[("Pildifailid", "*.png;*.jpg;*.jpeg")])
#     if file_path:
#         attach_entry.delete(0, END)
#         attach_entry.insert(0, file_path)

# # Tkinter
# win = Tk()
# win.title("E-kirja saatmine")
# win.geometry("700x400")
# win.configure(bg="white")

# Label(win, text="EMAIL:", bg="darkgreen", fg="white", font=("Arial", 12, "bold")).place(x=10, y=20)
# to_entry = Entry(win, width=40, bg="#eef2e1")
# to_entry.place(x=120, y=20)

# Label(win, text="TEEMA:", bg="darkgreen", fg="white", font=("Arial", 12, "bold")).place(x=10, y=60)
# subject_entry = Entry(win, width=40, bg="#eef2e1")
# subject_entry.place(x=120, y=60)

# Label(win, text="LISA:", bg="darkgreen", fg="white", font=("Arial", 12, "bold")).place(x=10, y=100)
# attach_entry = Entry(win, width=30, bg="#eef2e1")
# attach_entry.place(x=120, y=100)

# Button(win, text="LISA PILT", bg="darkgreen", fg="white", font=("Arial", 12), command=attach_image).place(x=460, y=100)

# Label(win, text="KIRI:", bg="darkgreen", fg="white", font=("Arial", 12, "bold")).place(x=10, y=140)
# message_text = Text(win, height=10, width=60, bg="#eef2e1")
# message_text.place(x=120, y=140)

# Button(win, text="SAADA", bg="darkgreen", fg="white", font=("Arial", 14, "bold"), command=send_email).place(x=560, y=330)

# image = Image.open("funnememe.png")
# image = image.resize((50, 50))
# photo = ImageTk.PhotoImage(image)
# img_label = Label(win, image=photo)
# img_label.image = photo
# img_label.place(x=530, y=20)

# win.mainloop()


# from tkinter import *
# from tkinter import filedialog, messagebox, ttk
# from PIL import Image, ImageTk
# import pygame
# import smtplib
# from email.message import EmailMessage
# import random
# import os
# import threading
# import time

# # --- Email Configuration ---
# GMAIL_USER = "tahmazovhussejn@gmail.com"
# GMAIL_APP_PASSWORD = "oxisfyxphjyfmdwi"
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587

# # --- Music Setup ---
# pygame.mixer.init()
# songs = ['opening.mp3', 'Hip_Hop.mp3']
# pygame.mixer.music.load(random.choice(songs))
# pygame.mixer.music.play(-1)

# # --- Tkinter Setup ---
# win = Tk()
# win.title("E-kirja saatmine")
# win.geometry("700x500")
# win.configure(bg="white")

# attachments = []  # Store multiple attachments

# # --- Functions ---
# def attach_files():
#     files = filedialog.askopenfilenames(
#         title="Vali failid",
#         filetypes=[("Kõik failid", "*.*")]
#     )
#     if files:
#         attachments.extend(files)
#         attachment_label.config(
#             text="\n".join([os.path.basename(f) for f in attachments])
#         )

# def send_email_thread():
#     threading.Thread(target=send_email).start()

# def send_email():
#     to_email = to_entry.get().strip()
#     subject = subject_entry.get().strip()
#     body = message_text.get("1.0", END).strip()

#     if not to_email or not subject or not body:
#         messagebox.showwarning("Tühjad väljad", "Palun täida kõik kohustuslikud väljad.")
#         return

#     # Reset and start progress bar
#     progress_bar["value"] = 0
#     win.update_idletasks()

#     msg = EmailMessage()
#     msg["From"] = GMAIL_USER
#     msg["To"] = to_email
#     msg["Subject"] = subject
#     msg.set_content(body)

#     total_files = len(attachments)
#     for i, file_path in enumerate(attachments):
#         if os.path.exists(file_path):
#             with open(file_path, "rb") as f:
#                 file_data = f.read()
#                 file_name = os.path.basename(file_path)
#                 msg.add_attachment(file_data,
#                                    maintype="application",
#                                    subtype="octet-stream",
#                                    filename=file_name)
#         # Simulate progress (or calculate based on actual file size/time)
#         progress_bar["value"] = int(((i + 1) / total_files) * 50)
#         win.update_idletasks()

#     try:
#         with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#             server.starttls()
#             progress_bar["value"] = 70
#             win.update_idletasks()

#             server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
#             progress_bar["value"] = 85
#             win.update_idletasks()

#             server.send_message(msg)
#             progress_bar["value"] = 100
#             win.update_idletasks()

#         messagebox.showinfo("Edu!", "E-kiri saadetud edukalt!")
#     except Exception as e:
#         progress_bar["value"] = 0
#         messagebox.showerror("Viga", f"Ei saanud kirja saata:\n{e}")

# # --- UI Layout ---
# Label(win, text="EMAIL:", bg="darkgreen", fg="white", font=("Arial", 12, "bold")).place(x=10, y=20)
# to_entry = Entry(win, width=40, bg="#eef2e1")
# to_entry.place(x=120, y=20)

# Label(win, text="TEEMA:", bg="darkgreen", fg="white", font=("Arial", 12, "bold")).place(x=10, y=60)
# subject_entry = Entry(win, width=40, bg="#eef2e1")
# subject_entry.place(x=120, y=60)

# Label(win, text="MANUSED:", bg="darkgreen", fg="white", font=("Arial", 12, "bold")).place(x=10, y=100)
# Button(win, text="VALI FAILID", bg="darkgreen", fg="white", font=("Arial", 12), command=attach_files).place(x=120, y=95)

# attachment_label = Label(win, text="(Pole valitud faile)", bg="white", fg="gray", justify=LEFT)
# attachment_label.place(x=250, y=100)

# Label(win, text="KIRI:", bg="darkgreen", fg="white", font=("Arial", 12, "bold")).place(x=10, y=150)
# message_text = Text(win, height=10, width=60, bg="#eef2e1")
# message_text.place(x=120, y=150)

# Button(win, text="SAADA", bg="darkgreen", fg="white", font=("Arial", 14, "bold"), command=send_email_thread).place(x=560, y=370)

# # Progress bar
# progress_bar = ttk.Progressbar(win, orient=HORIZONTAL, length=400, mode="determinate")
# progress_bar.place(x=120, y=350)

# # Meme image
# image = Image.open("funnememe.png")
# image = image.resize((50, 50))
# photo = ImageTk.PhotoImage(image)
# img_label = Label(win, image=photo)
# img_label.image = photo
# img_label.place(x=530, y=20)

# win.mainloop()


from tkinter import *
from tkinter import filedialog, messagebox, ttk, font
from PIL import Image, ImageTk
import pygame
import smtplib
from email.message import EmailMessage
import random
import os
import threading

# settings yada
GMAIL_USER = "tahmazovhussejn@gmail.com"
GMAIL_APP_PASSWORD = "oxisfyxphjyfmdwi"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# --- Music Setup :3 ---
pygame.mixer.init()
songs = ['opening.mp3', 'Hip_Hop.mp3']
pygame.mixer.music.load(random.choice(songs))
pygame.mixer.music.play(-1)

# tinker
win = Tk()
win.title("E-kirja saatmine")
win.geometry("800x600")
win.configure(bg="white")
win.iconbitmap("emailicon.ico")

attachments = []  # Store multiple attachments
current_font_family = "Arial"
current_font_size = 10
text_formats = {"bold": False, "italic": False}

# yo this sh aint bad?
def attach_files():
    selected = filedialog.askopenfilenames(
        title="Vali failid",
        filetypes=[("Kõik failid", "*.*")]
    )
    attachments.extend(selected)
    if attachments:
        names = []
    for f in attachments:
        names.append(os.path.basename(f))
        attachment_label.config(text="\n".join(names))

def send_email_thread():
    threading.Thread(target=send_email).start()

def send_email():
    to_email = to_entry.get().strip()
    subject = subject_entry.get().strip()
    body = message_text.get("1.0", END).strip()

    if not to_email or not subject or not body:
        messagebox.showwarning("Tühjad väljad", "Palun täida kõik kohustuslikud väljad.")
        return

    progress_bar["value"] = 0
    win.update_idletasks()

    msg = EmailMessage()
    msg["From"] = GMAIL_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    total_files = len(attachments)
    for i, file_path in enumerate(attachments):
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(file_path)
                msg.add_attachment(file_data,
                                 maintype="application",
                                 subtype="octet-stream",
                                 filename=file_name)
        progress_bar["value"] = int(((i + 1) / total_files) * 50)
        win.update_idletasks()

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            progress_bar["value"] = 70
            win.update_idletasks()

            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            progress_bar["value"] = 85
            win.update_idletasks()

            server.send_message(msg)
            progress_bar["value"] = 100
            win.update_idletasks()

        messagebox.showinfo("Edu!", "E-kiri saadetud edukalt!")
    except Exception as e:
        progress_bar["value"] = 0
        messagebox.showerror("Viga", f"Ei saanud kirja saata:\n{e}")

# New text formatting functions
def apply_formatting():
    # Get the current selection or insertion point
    try:
        sel_start = message_text.index(SEL_FIRST)
        sel_end = message_text.index(SEL_LAST)
    except TclError:
        # No selection, use insertion point
        sel_start = sel_end = message_text.index(INSERT)
    
    # Create font specification
    font_spec = []
    if text_formats["bold"]:
        font_spec.append("bold")
    if text_formats["italic"]:
        font_spec.append("italic")
    
    # Create font tuple
    font_tuple = (current_font_family, current_font_size, " ".join(font_spec))
    
    # Apply the tag to the selected text
    tag_name = f"font_{current_font_family}_{current_font_size}_{'_'.join(font_spec)}"
    message_text.tag_configure(tag_name, font=font_tuple)
    message_text.tag_add(tag_name, sel_start, sel_end)

def toggle_bold():
    # Toggle the bold formatting flag
    text_formats["bold"] = not text_formats["bold"]
    
    # Set the button relief based on the new state
    if text_formats["bold"]:
        relief = SUNKEN
    else:
        relief = RAISED

    bold_btn.config(relief=relief)

    # Apply the formatting changes to the text
    apply_formatting()

def toggle_italic():
    text_formats["italic"] = not text_formats["italic"]
    if text_formats["italic"]:
        relief = SUNKEN
    else:
        relief = RAISED

    italic_btn.config(relief=relief)
    apply_formatting()

def change_font(selected_font):
    global current_font_family
    current_font_family = selected_font
    apply_formatting()

def change_font_size(selected_size):
    global current_font_size
    current_font_size = int(selected_size)
    apply_formatting()

# --- UI Layout ---
# Email fields
Label(win, text="EMAIL:", bg="darkgreen", fg="white", font=("Arial", 12, "bold")).place(x=10, y=20)
to_entry = Entry(win, width=40, bg="#eef2e1")
to_entry.place(x=120, y=20)

Label(win, text="TEEMA:", bg="darkgreen", fg="white", font=("Arial", 12, "bold")).place(x=10, y=60)
subject_entry = Entry(win, width=40, bg="#eef2e1")
subject_entry.place(x=120, y=60)

Label(win, text="MANUSED:", bg="darkgreen", fg="white", font=("Arial", 12, "bold")).place(x=10, y=100)
Button(win, text="VALI FAILID", bg="darkgreen", fg="white", font=("Arial", 12), command=attach_files).place(x=120, y=95)

attachment_label = Label(win, text="(Pole valitud faile)", bg="white", fg="gray", justify=LEFT)
attachment_label.place(x=250, y=100)

# Text formatting toolbar
format_frame = Frame(win, bg="lightgray")
format_frame.place(x=120, y=130, width=500, height=30)

# Font family dropdown
font_families = ["Arial", "Times New Roman", "Courier New", "Verdana", "Helvetica"]
font_family_var = StringVar(value=current_font_family)
font_family_menu = OptionMenu(format_frame, font_family_var, *font_families, command=change_font)
font_family_menu.config(width=12)
font_family_menu.pack(side=LEFT, padx=2)

# Font size dropdown
font_sizes = [8, 10, 12, 14, 16, 18, 20, 24]
font_size_var = StringVar(value=str(current_font_size))
font_size_menu = OptionMenu(format_frame, font_size_var, *font_sizes, command=change_font_size)
font_size_menu.config(width=5)
font_size_menu.pack(side=LEFT, padx=2)

# Format buttons
bold_btn = Button(format_frame, text="B", font=("Arial", 10, "bold"), command=toggle_bold)
bold_btn.pack(side=LEFT, padx=2)

italic_btn = Button(format_frame, text="I", font=("Arial", 10, "italic"), command=toggle_italic)
italic_btn.pack(side=LEFT, padx=2)

# Message text area
Label(win, text="KIRI:", bg="darkgreen", fg="white", font=("Arial", 12, "bold")).place(x=10, y=170)
message_text = Text(win, height=12, width=70, bg="#eef2e1")
message_text.place(x=120, y=170)

# Set default font
default_font = font.Font(family=current_font_family, size=current_font_size)
message_text.configure(font=default_font)

# asdkakdakndaksdnkdknadkakjdkasdkn
Button(win, text="SAADA", bg="darkgreen", fg="white", font=("Arial", 14, "bold"), command=send_email_thread).place(x=650, y=450)

progress_bar = ttk.Progressbar(win, orient=HORIZONTAL, length=400, mode="determinate")
progress_bar.place(x=120, y=420)

# Meme image
image = Image.open("funnememe.png")
image = image.resize((80, 80))
photo = ImageTk.PhotoImage(image)
img_label = Label(win, image=photo)
img_label.image = photo
img_label.place(x=700, y=20)

win.mainloop()