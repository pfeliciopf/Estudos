import time

while True:
    hora = time.strftime("%H:%M:%S")
    
    print(hora, end="\r")
    
    time.sleep(1)