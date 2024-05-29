import customtkinter as ttk
import tkinter as tk
from tkinter import *
import yfinance
import time
start_app = ttk.CTk()
start_app.title("Start Page")
label_var = tk.StringVar()

counter = 0
def update_label():
    global counter

    bitcoin = yfinance.Ticker('BTC-EUR')
    bitcoin_value = bitcoin.basic_info

    ETH = yfinance.Ticker('ETH-EUR')
    ETH_value = ETH.basic_info

    XMR = yfinance.Ticker('XMR-EUR')
    XMR_value = XMR.basic_info

    XRP = yfinance.Ticker('XRP-EUR')
    XRP_value = XRP.basic_info

    DOGE = yfinance.Ticker('DOGE-EUR')
    DOGE_value = DOGE.basic_info

    LTC = yfinance.Ticker('DOGE-EUR')
    LTC_value = LTC.basic_info
    counter += 1
    label_var.set(f'1BTC = {bitcoin_value.last_price:.2f} {bitcoin_value.currency}\n'
                  f'1ETH = {ETH_value.last_price:.2f} {ETH_value.currency}\n'
                  f'1Monero = {XMR_value.last_price:.2f} {XMR_value.currency}\n'
                  f'1XRP = {XRP_value.last_price:.2f} {XRP_value.currency}\n'
                  f'1Dogecoin = {DOGE_value.last_price:.2f} {DOGE_value.currency}\n'             
                  f'1Litecoin = {LTC_value.last_price:.2f} {LTC_value.currency}\n')

    start_app.after(30000, update_label) #10000ms = 10sec

    # Gibt in die Console an wie oft es aktualisiert wird-/
    print(f"Ubdate_label wurde zum {counter} wiederholt")


def button_function():
    start_app.destroy()

ttk.set_appearance_mode("dark")
ttk.set_default_color_theme("blue")

frame = ttk.CTkFrame(master=start_app,
                     width=900,
                     height=650,
                     fg_color="white",
                     bg_color="gray15",
                     corner_radius=20,
                     )
frame.pack(padx=20, pady=20)

button_logout = ttk.CTkButton(master=frame,
                              corner_radius=10,
                              text="Quit",
                              fg_color="turquoise4",
                              bg_color="white",
                              command = button_function,
                              width=230,
                              height=40
                              )
button_logout.place(relx=0.73, rely=0.93, anchor = tk.CENTER,)

wid = ttk.CTkLabel(master=frame,
                     text="",
                     corner_radius=20,
                     fg_color="Gray50",
                     bg_color="white",
                     width=350,
                     height=600,
                     )
wid.place(relx=0.23, rely=0.5, anchor=CENTER)

label = ttk.CTkLabel(master=frame,
                     text="Währungen",
                     corner_radius=0,
                     fg_color="Gray50",
                     width=300,
                     height=50,
                     font=('times', 25, 'bold', 'italic','underline')
                     )
label.place(relx=0.23, rely=0.08, anchor=CENTER)

label = ttk.CTkLabel(master=frame,
                     textvariable = label_var,
                     corner_radius=0,
                     fg_color="gray50",
                     bg_color="white",
                     width=200,
                     height=50,
                     font=('times', 25, 'bold')
                     )
label.place(relx=0.23, rely=0.35, anchor=CENTER)



update_label()
start_app.mainloop()