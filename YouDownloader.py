# Importing modules
from pytube import YouTube
import customtkinter
from distutils.core import setup
import py2exe

# GUI settings
mode = customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App settings
app =  customtkinter.CTk()
app.geometry("460x250")
app.resizable(False, False)
app.title("YouDownloader")
app.iconbitmap("icon.ico")

# Download command
def download():
    try:
        youtube_link = URL_entry.get()
        youtube_object = YouTube(youtube_link)
        video = youtube_object.streams.get_highest_resolution()
        video.download()
        text.configure(text="Download complete!")
    except:
        text.configure(text="Something went wrong, \ncheck your internet connection, and the YouTube link")

# UI (Text, button, entry...)
title = customtkinter.CTkLabel(app, text="YouDownloader", pady=20,font=("sans-serif", 40))
url_var = customtkinter.StringVar()
URL_entry = customtkinter.CTkEntry(app, width=400, height=30, corner_radius=10, textvariable=url_var, font=('sans-serif', 20))
text = customtkinter.CTkLabel(app, text="Ctrl+V to paste your youtube link", pady=20,font=("sans-serif", 19))
submit_button = customtkinter.CTkButton(app, text="Download", fg_color="#F44336", hover_color="#E53935", command=download)

# Applying the UI to the app
title.pack()
URL_entry.pack()
text.pack()
submit_button.pack()

# Running the app
app.mainloop()