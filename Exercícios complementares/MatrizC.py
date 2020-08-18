def main():
# Matriz preenchida
    #matrizC = [[39, 14, 27], [21, 83, 92], [31, 12, 43]]

# Inserindo os valores na matriz
    matrizC = []

    for i in range(3):
        valores = []
        for j in range(3):
            valores.append(input('Digite um número: '))
        matrizC.append(valores)
    #print(matrizC)

# Removendo os itens de cada linha
    for i in range(len(matrizC)):
        del (matrizC[i][len(matrizC[i])-1])

    print(matrizC)


main()