import tkinter as tk
import customtkinter as ttk
from tkinter import *

def button_event():
    if ((user_id_entry.get() == user_id) and (password_entry.get() == password)
            or (user_id_entry.get() == user_id1) and (password_entry.get() == password1)) :
        text_var.set("Connected")
        app.destroy()
        import start_page
    else:
        text_var.set("Wrong Password oder User_ID")

ttk.set_appearance_mode("System")
ttk.set_default_color_theme("blue")

app = ttk.CTk()
app.title("Zerschta")
app.overrideredirect(True)

def move_window(event):
    app.geometry(f"+{event.x_root}+{event.y_root}")
# Binde die Funktion an das Titelleisten-Event
app.bind("<B1-Motion>", move_window)

frame = ttk.CTkFrame(master=app,
                     width=300,
                     height=250,
                     fg_color="white",
                     bg_color="green",
                     corner_radius=10,
                     )
frame.pack(padx=20, pady=20)

user_id_entry = ttk.CTkEntry(master=frame,
                             placeholder_text="User ID",
                             width= 150,
                             height= 30,
                             border_width = 2,
                             corner_radius = 10
                             )
user_id_entry.place(relx=0.5, rely=0.2, anchor = ttk.CENTER)

password_entry = ttk.CTkEntry(master=frame,
                              placeholder_text="Password",
                              width=150,
                              height=30,
                              show="*",
                              border_width=2,
                              corner_radius=10
)

password_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

user_id = "Zerschta"
password = "Admin"

user_id1 = "1"
password1 = "1"

button = ttk.CTkButton(master=frame,
                       corner_radius=10,
                       bg_color="white",
                       fg_color="turquoise4",
                       text ="ENTER",
                       command=button_event)
button.place(relx=0.5, rely=0.6, anchor = tk.CENTER)


text_var = StringVar()

label = ttk.CTkLabel(master=frame,
                     textvariable =text_var,
                     width=120,
                     height=25,
                     fg_color=("white", "gray75"),
                     corner_radius=8)
label.place(relx=0.5, rely=0.75, anchor = tk.CENTER)



app.mainloop()

