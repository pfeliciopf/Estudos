from tkinter import *
import random
import time

janela = Tk()
janela.geometry("400x400")

cores = ["red", "blue", "green", "yellow", "purple", "orange", "black", "white"]

while True:
    cor_aleatoria = random.choice(cores)
    janela.configure(bg=cor_aleatoria)
    janela.update()
    time.sleep(0.5)
