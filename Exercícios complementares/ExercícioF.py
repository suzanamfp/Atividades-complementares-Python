def main():
    listaNomes = []

    for i in range(0, 5):
        nomes = str(input("Digite um nome: "))
        listaNomes.append(nomes)
    print(listaNomes)

    sobrenome = str(input("Digite seu sobrenome: "))
    listaNomes.insert(0, sobrenome)
    print(listaNomes)


main()


