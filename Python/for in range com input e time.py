import time

n=int(input("escolha um número: "))
n2=int(input("escolha outro número: "))
for i in range (n, n2):
    time.sleep(0.01)
    print (f"número- {i}")