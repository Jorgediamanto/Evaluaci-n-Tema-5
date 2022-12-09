import datetime

now = datetime.datetime.now()
print("Hora actual es: ")
print(now.strftime("%H:%M:%S"))
x=now.strftime("%H:%M:%S")


while True:
    if x!=now.strftime("%H:%M:%S"):
        print(now.strftime("%H:%M:%S"))
        x=now.strftime("%H:%M:%S")