def main():
    registro = []

    for i in range (0, 5):
        nome = str(input("Digite um nome: "))
        registro.append(nome)
    print (registro)

    novoNome = str(input("Digite um novo nome: " ))
    registro.append(novoNome)

    novoNome2 = str(input("Digite um novo nome: "))
    registro.insert(2, novoNome2)
    print(registro)

main()
