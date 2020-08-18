def main():
    matriz3 = []

    for i in range (3):
        valores =[]
        nome = input(input("Digite um nome: "))
        dataNascimento = (input("Digite uma data de nascimento: "))
        matricula = (input("Digite uma matrícula: "))
        for j in range (1):
            valores.append(nome)
            valores.append(dataNascimento)
            valores.append(matricula)
        matriz3.append(valores)
    print(matriz3)






main()