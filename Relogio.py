import random
import time
from datetime import datetime as dt
import tkinter as tk


Data=dt.now()
#print(data)

Hora=0
Minuto=0
Segundo=0

Hora=Data.hour
Minuto=Data.minute
Segundo=Data.second

HoraAtual=Data.strftime('%d/%m/%y - %H:%M:%S')
print(HoraAtual)

while True:
    time.sleep(1)
    Data =dt.now()
    HoraAtual = Data.strftime('%d/%m/%y - %H:%M:%S')
    print(HoraAtual)
    
## Fazendo relogio contar os segundos do momento em que foi iniciado