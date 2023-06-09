# Importing necessary modules
from pytube import YouTube
import customtkinter

# GUI settings
mode = customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# App settings
app =  customtkinter.CTk()
app.geometry("450x240")
app.title("YouDownloader")
app.wm_iconbitmap("icon.ico")

# Download command
def download():
    try:
        youtube_link = URL_entry.get()
        youtube_object = YouTube(youtube_link)
        video = youtube_object.streams.get_highest_resolution()
        video.download()
    except:
        error = customtkinter.CTkLabel(app, text="Something went wrong, \ncheck your internet connection, and the YouTube link", font=("sans-serif", 20)).pack()

# UI (Text, button, entry...)
title = customtkinter.CTkLabel(app, text="YouDownloader", pady=20,font=("sans-serif", 40))
url_var = customtkinter.StringVar()
URL_entry = customtkinter.CTkEntry(app, width=400, height=30, border_width=0, corner_radius=10, textvariable=url_var, font=('sans-serif', 20))
text = customtkinter.CTkLabel(app, text="Ctrl+V or ⌘+V to paste your youtube link", pady=20,font=("sans-serif", 18))
submit_button = customtkinter.CTkButton(app, text="Download", command=download)
finish_text = customtkinter.CTkLabel(app, text="", font=("sans-serif", 20))


# Applying the UI to the app
title.pack()
URL_entry.pack()
text.pack()
submit_button.pack()
finish_text.pack()

# Running the app
app.mainloop()