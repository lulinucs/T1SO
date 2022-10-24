import random
import threading
import time
from tkinter import *

class Ficha:
    def __init__(self):
        self.posicao = None

class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.estado = ' '

def gerar_tabuleiro():
    matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    i = 1


    for l in range(10):
        for c in range(10):
            casa = Casa(i)
            matriz[l][c] = casa
            i+=1

    return matriz


def mostrar_tabuleiro(tabuleiro):
    for l in range(10):
        for c in range (10):
            print(f'[{tabuleiro[l][c].estado}]', end='')
        print()
    print(ficha1.posicao)
    print(ficha2.posicao)
    print(ficha3.posicao)
    print(ficha4.posicao)
    print(ficha5.posicao)
    print()

def movimentar_ficha(tabuleiro, ficha):
        linha = random.randrange(0, 9)
        coluna = random.randrange(0, 9)
        tabuleiro[linha][coluna].estado = 'X'
        ficha.posicao = tabuleiro[linha][coluna].endereco

def movimentar_fichas_simultaneamente_easy(tabuleiro, ficha1, ficha2, ficha3, ficha4, ficha5, janela):
    rodada = 0
    while(1):
        limpa_tabuleiro(tabuleiro)
        thread1 = threading.Thread(target=movimentar_ficha, args=(tabuleiro, ficha1,))
        thread2 = threading.Thread(target=movimentar_ficha, args=(tabuleiro, ficha2,))
        thread3 = threading.Thread(target=movimentar_ficha, args=(tabuleiro, ficha3,))
        thread4 = threading.Thread(target=movimentar_ficha, args=(tabuleiro, ficha4,))
        thread5 = threading.Thread(target=movimentar_ficha, args=(tabuleiro, ficha5,))
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        mostrar_tabuleiro(tabuleiro)

        i = 0

        if rodada == 0 :
            casa = []
        for l in range(10):
            for c in range(10):
                text = tabuleiro[l][c].estado
                if rodada == 0:
                    casa.append(Button(janela, text=text))
                    casa[i].grid(column=c, row=l, padx=10, pady=10)
                else:
                    casa[i]["text"] = text
                i += 1
        rodada += 1

        time.sleep(5000)

def limpa_tabuleiro(tabuleiro):
    for l in range(10):
        for c in range(10):
           tabuleiro[l][c].estado = ' '


janela = Tk()
janela.title("Joguinho Paia")

tabuleiro = gerar_tabuleiro()
ficha1 = Ficha()
ficha2 = Ficha()
ficha3 = Ficha()
ficha4 = Ficha()
ficha5 = Ficha()



thread6 = threading.Thread(target=movimentar_fichas_simultaneamente_easy, args=(tabuleiro, ficha1, ficha2, ficha3, ficha4, ficha5, janela, ))

thread6.start()
janela.mainloop()




