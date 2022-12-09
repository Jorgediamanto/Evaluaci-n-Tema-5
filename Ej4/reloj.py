import datetime
import os



now = datetime.datetime.now()

print(now.strftime("%H:%M:%S"))
x=now.strftime("%H:%M:%S")


while True:
    now = datetime.datetime.now()
    
    if x!=now.strftime("%H:%M:%S"):
        os.system('cls')
        print("Hora actual es: ")
        print(now.strftime("%H:%M:%S"))
        x=now.strftime("%H:%M:%S")
        

