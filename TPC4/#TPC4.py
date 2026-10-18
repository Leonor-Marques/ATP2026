import random

lista = []
opcao = -1

while opcao != 0:
    print("\n----- MENU -----")
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        n = int(input("Quantos elementos quer na lista? "))
        lista = []

        for i in range(n):
            numero = random.randint(1, 100)
            lista.append(numero)

        print("Lista criada:", lista)

    elif opcao == 2:
        n = int(input("Quantos elementos quer introduzir? "))
        lista = []

        for i in range(n):
            numero = int(input("Introduza um número inteiro: "))
            lista.append(numero)

        print("Lista criada:", lista)

    elif opcao == 3:
        soma = 0

        for i in range(len(lista)):
            soma = soma + lista[i]

        print("Soma dos elementos:", soma)

    elif opcao == 4:
        if len(lista) > 0:
            soma = 0

            for i in range(len(lista)):
                soma = soma + lista[i]

            media = soma / len(lista)
            print("Média dos elementos:", media)
        else:
            print("A lista está vazia.")

    elif opcao == 5:
        if len(lista) > 0:
            maior = lista[0]

            for i in range(1, len(lista)):
                if lista[i] > maior:
                    maior = lista[i]

            print("Maior elemento:", maior)
        else:
            print("A lista está vazia.")

    elif opcao == 6:
        if len(lista) > 0:
            menor = lista[0]

            for i in range(1, len(lista)):
                if lista[i] < menor:
                    menor = lista[i]

            print("Menor elemento:", menor)
        else:
            print("A lista está vazia.")

    elif opcao == 7:
        crescente = True

        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                crescente = False

        if crescente:
            print("Sim, a lista está ordenada por ordem crescente.")
        else:
            print("Não, a lista não está ordenada por ordem crescente.")

    elif opcao == 8:
        decrescente = True

        for i in range(len(lista) - 1):
            if lista[i] < lista[i + 1]:
                decrescente = False

        if decrescente:
            print("Sim, a lista está ordenada por ordem decrescente.")
        else:
            print("Não, a lista não está ordenada por ordem decrescente.")

    elif opcao == 9:
        numero = int(input("Que número pretende procurar? "))
        posicao = -1

        for i in range(len(lista)):
            if lista[i] == numero and posicao == -1:
                posicao = i

        if posicao != -1:
            print("Elemento encontrado na posição:", posicao)
        else:
            print("Elemento não encontrado. Posição:", posicao)

    elif opcao == 0:
        print("Programa terminado.")
        print("Lista final:", lista)

    else:
        print("Opção inválida.")

input("Prima Enter para terminar.")
