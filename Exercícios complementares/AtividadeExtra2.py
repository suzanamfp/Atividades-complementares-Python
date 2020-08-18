def main():
    matriz2 = []

    for i in range(2):
        numeros = []
        for j in range(2):
            numeros.append(input('Digite um número: '))
        matriz2.append(numeros)
    print(matriz2)

    cont=0
    for i in range(len(matriz2)):
        for numeros in i:
            if numeros > 10:
                cont = cont +1
            print(cont)







main()