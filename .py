import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

#galvenā loga izveide
logs = Tk()
logs.geometry("350x400")
logs.title("Instrumentu noma")
logs.configure(background = "#FFE1E9")

logo_frame = tk.Frame(logs)
logo_frame.grid(row=6, column=0, columnspan=5, padx=10)
logo_image = Image.open("garff.png")
resized_logo = logo_image.resize((125,125))
logo = ImageTk.PhotoImage(resized_logo)
logo_label = ttk.Label(logo_frame, image=logo)
logo_label.grid(row=6, column=1,columnspan=5, padx=10)

#pogas galvenajā logā
btn=Button(logs, text="Pasūtījums",bd="5", command = lambda: pasutijums())
btn1=Button(logs, text="Aizvērt!", bd="5", command=logs.destroy)
btn.grid(row=1, column=3, padx=25, pady=25)
btn1.grid(row=1, column=5, padx=25, pady=25)

def pasutijums():
    logs1=Toplevel()
    logs1.geometry("350x350")
    logs1.title("Pasūtījums")

    ttk.Label(logs1, text="Izvēlies darbinieku:").grid(column = 0, row = 0, padx=20, pady=25)
    ttk.Label(logs1, text="Izvēlies instrumentu:").grid(column = 0, row = 1, padx=20, pady=25)
    ttk.Label(logs1, text="Norādi cenu:").grid(column = 0, row = 2, padx=20, pady=25)
    ttk.Label(logs1, text="Nomas dienas:").grid(column = 0, row = 3, padx=20, pady=25)
    #mainīgie
    vardsuzvards = tk.StringVar()
    instruments = tk.StringVar()
    cena = tk.StringVar()
    dienas = tk.StringVar()
    #izvēles izveide
    darbinieki = ttk.Combobox(logs1, textvariable=vardsuzvards)
    instrumenti = ttk.Combobox(logs1, textvariable=instruments)
    nomascena = ttk.Combobox(logs1, textvariable=cena)
    nomasdienas = ttk.Entry(logs1, textvariable=dienas)
    darbinieki['values'] = ("Kārlis Bērziņš", "Pēteris Zāle", "Jānis Čakste", "Sanija Priede")
    instrumenti['values'] = ('frēze', 'slīpmašina', 'urbis')
    nomascena['values'] = ('15', '55', '10')

    darbinieki.grid(column=1, row=0)
    instrumenti.grid(column=1, row=1)
    nomascena.grid(column=1, row=2)
    nomasdienas.grid(column=1, row=3)







logs.mainloop()

