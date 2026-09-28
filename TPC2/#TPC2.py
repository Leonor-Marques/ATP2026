#TP2
## Modalidade 1
from random import randint
computador = randint(0, 100)
jogador = int(input("Em que número estou a pensar?")) 
tentativas = 0

while jogador != computador:
    if jogador < computador:
        print("é maior!")
        jogador = int(input("Em que número estou a pensar?")) 
        tentativas = tentativas + 1
    elif jogador > computador:
        print("é menor!")
        jogador = int(input("Em que número estou a pensar?"))
        tentativas = tentativas + 1 

tentativas = tentativas + 1
print(f"Acertou em {tentativas} tentativas")

## Modalidade 2
print("Pensa num número de 0 a 100, no caso de eu não acertar tens de dizer se o número é maior ou menor.")
min = 0
max = 100
tentativas = 0
palpite = int((min + max)/2)
print(palpite)
resposta = input("Está certo?")

while resposta != "acertou":
    if resposta == "maior":
        min = palpite + 1
        palpite = int((min + max)/2)
        print(palpite)
        resposta = input("Está certo?")
        tentativas = tentativas + 1
    elif resposta == "menor":
        max = palpite - 1
        palpite = int((min + max)/2)
        print(palpite)
        resposta = input("Está certo?")
        tentativas = tentativas + 1
tentativas = tentativas + 1
print (f"Acertei em {tentativas} tentativas")
