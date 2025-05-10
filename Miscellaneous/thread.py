

import tkinter as tk
from tkinter import messagebox
import threading
import time

curr_resistance = 0
heater_dc = 28
exp_snsr_resistance = 45

def get_curr_resistance():
    global curr_resistance
    
    curr_resistance = int(entry.get())
    # Mostrar el valor actualizado en el label
    label_current.config(text=f"Current Resistance actual: {curr_resistance}")
    entry.delete(0, tk.END) 

def ajustar_heater_dc():
    global heater_dc, curr_resistance
    while True:
        if curr_resistance > exp_snsr_resistance:
            heater_dc += 0.1  
            time.sleep(2)
            #WrafSnsrHtr_dc.set(heater_dc)
        if curr_resistance < 40:
            heater_dc -= 0.1  
            time.sleep(2)  
        label_heater.config(text=f"Heater DC: {heater_dc}")
        time.sleep(1)  


root = tk.Tk()
root.title("Input")


entry = tk.Entry(root)
entry.pack(pady=10)


button = tk.Button(root, text="Actualizar Valor", command=get_curr_resistance)
button.pack(pady=5)


label_current = tk.Label(root, text=f"Current Resistance actual: {curr_resistance}")
label_current.pack(pady=10)

label_heater = tk.Label(root, text=f"Heater DC: {heater_dc}")
label_heater.pack(pady=10)

hilo_ajuste = threading.Thread(target=ajustar_heater_dc, daemon=True)
hilo_ajuste.start()

root.mainloop()