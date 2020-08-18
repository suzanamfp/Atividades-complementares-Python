def main():

    amigos = ['Luana', 'Caio', 'Ana', 'Maria']

    datasAniversario = ['06.11','15.06', '29.08', '13.07']

    amigos.remove('Ana')
    datasAniversario.remove('29.08')
    print(amigos)
    print(datasAniversario)

    amigos.append('Lorena')
    datasAniversario.append('31.12')
    print(amigos)
    print(datasAniversario)

    quantidadeA = int(input("Quantos nomes você precisa inserir?"))
    for i in range(0, quantidadeA):
        novoAmigo = (input("Insira um novo nome: "))
        amigos.append(novoAmigo)
    print(amigos)

    quantidadeD = int(input("Quantos datas você precisa inserir?"))
    for i in range(0, quantidadeD):
        novaData = (input("Insira uma nova data: "))
        datasAniversario.append(novaData)
    print(datasAniversario)



main()