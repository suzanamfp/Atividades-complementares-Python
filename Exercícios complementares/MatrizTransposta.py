def main():
    matriz= []
    matrizT= []


    linha = int(input("Digite a quaantidade de linhas: "))
    coluna = int(input("Digite a quaantidade de colunas: "))
    for an in range(0,linha):
        valores = []
        for n in range(0,coluna):
            valores.append(input("Digite um número: "))
        matriz.append(valores)


    print(matriz)

    # Fazendo a matriz ficar transposta
    for n in range(coluna):
        valores = []
        for an in range(linha):
            valores.append(matriz[an][n])
        matrizT.append(valores)


    print(matrizT)




main()