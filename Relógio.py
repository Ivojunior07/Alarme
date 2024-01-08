import random
import tkinter as tk
from tkinter import messagebox
from time import strftime, sleep
from threading import Thread #fazer 2 coisas ao mesmo tempo 
from datetime import datetime

def set_alarm():
    alarm_hour = int(entry_hour.get())
    alarm_min = int(entry_min.get())
    alarm_second = int(entry_second.get())

    try:
        if alarm_hour < 0 or alarm_hour > 23 or alarm_min < 0 or alarm_min > 59 or alarm_second < 0 or alarm_second > 59:
            raise ValueError
    except ValueError:
        messagebox.showerror('Formato de tempo inválido')
        return

    alarm_time = f'{alarm_hour:02d}:{alarm_min:02d}:{alarm_second:02d}'

    while True:
        current_time = strftime('%H:%M:%S')
        live_clock_label.config(text='Hora atual' + current_time)
        if current_time == alarm_time:
            messagebox.showinfo('ALARME, HORA DE ACORDAR') # pode adicionar para tocar música ou algo do tipo
            break
        root.update()
        sleep(1)

def update_live_clock():
    while True:
        current_time = strftime('%H:%M:%S')
        live_clock_label.config(text='Hora atual' + current_time)
        root.update()
        sleep(1)

root = tk.Tk()
root.title('Alarm system')

frame = tk.Frame(root)
frame.pack(padx=20 , pady=20)

live_clock_label = tk.Label(frame, text='Hora atual: '+ strftime('%H:%M:%S'))
live_clock_label.grid(row=0, column=0, columnspan=3)

lable_hour = tk.Label(frame, text='Hora:')
lable_hour.grid(row=1, column=0, sticky='W')

entry_hour = tk.Entry(frame)
entry_hour.grid(row=1, column=1)

lable_min = tk.Label(frame, text='Minuto:')
lable_min.grid(row=2, column=0, sticky='W')

entry_min = tk.Entry(frame)
entry_min.grid(row=2, column=1)

lable_second = tk.Label(frame, text='Segundo:')
lable_second.grid(row=3, column=0, sticky='W')

entry_second = tk.Entry(frame)
entry_second.grid(row=3, column=1)

button_set_alarm = tk.Button(frame, text='Definir Hora', command=set_alarm)
button_set_alarm.grid(row=4, column=0, columnspan=3)


live_clock_thread = Thread(target=update_live_clock)
live_clock_thread.daemon = True
live_clock_thread.start()

root.mainloop()
