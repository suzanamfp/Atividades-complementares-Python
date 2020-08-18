
def main():
    tabuleiro = [["1","2","3"],["4","5","6"], ["7","8","9"]]


    print("Jogador 1 = X")
    print("Jogador 2 = O")
    quantJogadas = 1

    jogador = "X"
    while True:
        if (quantJogadas>9):
            print("Ninguém ganhou!")
            break

        for i in range(3):
            print(tabuleiro[i][0], "|", tabuleiro[i][1], "|", tabuleiro[i][2])

        if quantJogadas>4 and validacaoJogo(tabuleiro) == True:
            break

        jogada = str(input ("Jogador " + jogador + ". Digite a posição: "))

        for i in range(3):
            for n in range(3):
                if tabuleiro[i][n] == jogada:
                    tabuleiro[i][n] = jogador

        if jogador == "X":
            jogador = "O"
        elif jogador == "O":
            jogador = "X"

        quantJogadas = quantJogadas + 1

def validacaoJogo(tabuleiro):

    ret = False
    for i in range(len(tabuleiro)):
        qtdO = 0
        qtdX = 0
        for j in range (len (tabuleiro)):
            if tabuleiro[i][j] == "X":
                qtdX = qtdX+1
            if tabuleiro[i][j] == "O":
                qtdO = qtdO+1

        if qtdX==3:
            print("Jogador X Ganhou!")
            ret = True
            break
        elif qtdO==3:
            print("Jogador O Ganhou!")
            ret = True
            break

        qtd0 = 0
        qtdX = 0
        for j in range(len(tabuleiro)):
            if tabuleiro[j][i] == "X":
                qtdX = qtdX+1
            if tabuleiro[j][i] == "O":
                qtd0 = qtd0+1

        if qtdX==3:
            print("Jogador X Ganhou!")
            ret = True
            break
        elif qtd0==3:
            print("Jogador O Ganhou!")
            ret = True
            break

        if tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X":
            print("Jogador X Ganhou!")
            ret = True
            break
        elif tabuleiro[0][2] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][0] == "X":
            print("Jogador X Ganhou!")
            ret = True
            break
        elif tabuleiro[0][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O":
            print("Jogador O Ganhou!")
            ret = True
            break
        elif tabuleiro[0][2] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][0] == "O":
            print("Jogador O Ganhou!")
            ret = True
            break

    return ret

main()