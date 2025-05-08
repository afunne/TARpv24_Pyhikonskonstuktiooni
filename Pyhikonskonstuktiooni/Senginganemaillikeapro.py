# from tkinter import *
# # from PIL import ImageTk, Image

# # # main settings
# aken = Tk()
# aken.title("MatimatikaFORrealMEN")
# aken.geometry("600x300")
# aken.configure(bg="white")
# aken.iconbitmap("Clover_overworld.ico")
# aken.resizable(False, False)

# # # testing if things exist
# # help('PIL')

# # # how labels will look like
# # image1 = Image.open("<C:\Users\opilane\Downloads\static-assets-upload10060524083770360299.webp>")

# img = PhotoImage(file="funnememe.png")
# resized_image = img.resize((250, 200))
# Deathwing2=aken.PhotoImage(resized_image)

# aken.mainloop()



# Import the required libraries
from tkinter import *
from PIL import Image, ImageTk
from playsound import playsound
import random
# import required module
file=['opening.mp3', 'Hip_Hop.mp3']
random_ost=random.choice(file)


def play():
    playsound(random_ost, block=False)


# Create an instance of tkinter frame or window
win=Tk()
win.title("EmailSender ")
# Set the size of the tkinter window
win.geometry("700x350")


# Load the image
image=Image.open('funnememe.png')

# Resize the image in the given (width, height)
img=image.resize((150, 150))

# Conver the image in TkImage
my_img=ImageTk.PhotoImage(img)

# Display the image with label
label=Label(win, image=my_img)
label.place(x=490, y=60)

play()
win.mainloop()