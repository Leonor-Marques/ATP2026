total = 0

modo = int(input("Escolha a modalidade (1 - computador joga primeiro / 2 - jogador joga primeiro): "))

if modo == 1:
    # Computador começa
    computador = 1
    total = total + computador
    print("Computador:", computador)
    print("Total:", total)

    while total < 100:
        jogador = int(input("Escolha um número de 1 a 10: "))

        while jogador < 1 or jogador > 10:
            jogador = int(input("Número inválido. Escolha um número de 1 a 10: "))

        total = total + jogador
        print("Jogador:", jogador)
        print("Total:", total)

        if total == 100:
            print("Ganhou o jogador!")
            break

       
        computador = 11 - jogador
        total = total + computador

        print("Computador:", computador)
        print("Total:", total)

        if total == 100:
            print("Ganhou o computador!")


elif modo == 2:
    # Jogador começa
    while total < 100:
        jogador = int(input("Escolha um número de 1 a 10: "))

        while jogador < 1 or jogador > 10:
            jogador = int(input("Número inválido. Escolha um número de 1 a 10: "))

        total = total + jogador
        print("Jogador:", jogador)
        print("Total:", total)

        if total == 100:
            print("Ganhou o jogador!")
            break

        
        computador = 11 - jogador
        total = total + computador

        print("Computador:", computador)
        print("Total:", total)

        if total == 100:
            print("Ganhou o computador!")
            break

else:
    print("Modo inválido.")
