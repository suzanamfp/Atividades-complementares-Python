def main():

    matriz1=[[1,2,3,4],[5,6,7,8]]

    print(matriz1)
    for linha in range (len(matriz1)):
        novoValor = input("Qual valor você deseja inserir?")
        matriz1.append(novoValor)
    print(matriz1)


main()