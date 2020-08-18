import random
def main():

    opcoes = ["pedra", "papel", "tesoura", "lagarto", "Spock"]
    jogadores = ["Sheldon", "Raj"]

    opcoesSheldon = []
    opcoesRaj = []

    teste = int(input("Digite um número de teste: "))
    for i in range(0, teste):
        opcoesSheldon.append(random.randint(0,len(opcoes)-1))
        opcoesRaj.append(random.randint(0, len(opcoes)-1))

    print('SHELDON                                    RAJ                             RESULTADO')
    for i in range (0, teste):

        opcaoS = opcoesSheldon[i]
        opcaoR = opcoesRaj[i]
        resultado = ""

        #01
        if (opcoes[opcaoS] == "tesoura") and (opcoes[opcaoR]=="papel"):
            resultado = "Bazinga!"
        elif (opcoes[opcaoR] == "tesoura") and (opcoes[opcaoS] == "papel"):
            resultado = "Raj trapaceou"
        #02
        elif (opcoes[opcaoS] == "papel") and (opcoes[opcaoR]=="pedra"):
            resultado = "Bazinga!"
        elif (opcoes[opcaoR] == "papel") and (opcoes[opcaoS] == "pedra"):
            resultado = "Raj trapaceou"
        #03
        elif (opcoes[opcaoS] == "pedra") and (opcoes[opcaoR]=="lagarto"):
            resultado = "Bazinga!"
        elif (opcoes[opcaoR] == "pedra") and (opcoes[opcaoS] == "lagarto"):
            resultado = "Raj trapaceou"
        #04
        elif (opcoes[opcaoS] == "lagarto") and (opcoes[opcaoR]=="Spock"):
            resultado = "Bazinga!"
        elif (opcoes[opcaoR] == "lagarto") and (opcoes[opcaoS] == "Spock"):
            resultado = "Raj trapaceou"
        #05
        elif (opcoes[opcaoS] == "Spock") and (opcoes[opcaoR]=="tesoura"):
            resultado = "Bazinga!"
        elif (opcoes[opcaoR] == "Spock") and (opcoes[opcaoS] == "tesoura"):
            resultado = "Raj trapaceou"
        #06
        elif (opcoes[opcaoS] == "tesoura") and (opcoes[opcaoR]=="lagarto"):
            resultado = "Bazinga!"
        elif (opcoes[opcaoR] == "tesoura") and (opcoes[opcaoS] == "lagarto"):
            resultado = "Raj trapaceou"
        #07
        elif (opcoes[opcaoS] == "lagarto") and (opcoes[opcaoR]=="papel"):
            resultado = "Bazinga!"
        elif (opcoes[opcaoR] == "lagarto") and (opcoes[opcaoS] == "papel"):
            resultado = "Raj trapaceou"
        #08
        elif (opcoes[opcaoS] == "papel") and (opcoes[opcaoR]=="Spock"):
            resultado = "Bazinga!"
        elif (opcoes[opcaoR] == "papel") and (opcoes[opcaoS] == "Spock"):
            resultado = "Raj trapaceou"
        #09
        elif (opcoes[opcaoS] == "Spock") and (opcoes[opcaoR]=="pedra"):
            resultado = "Bazinga!"
        elif (opcoes[opcaoR] == "Spock") and (opcoes[opcaoS] == "pedra"):
            resultado = "Raj trapaceou"
        #10
        elif (opcoes[opcaoS] == "pedra") and (opcoes[opcaoR]=="tesoura"):
            resultado = "Bazinga!"
        elif (opcoes[opcaoR] == "pedra") and (opcoes[opcaoS] == "tesoura"):
            resultado = "Raj trapaceou"
        else :
            resultado = "De novo!"

        resultado = "Caso #" + (str) (i +1) + " " + resultado
        espacos = ""
        qtdCaracteres = 43 - len(opcoes[opcoesSheldon[i]])
        for c in range (0, qtdCaracteres):
            espacos += " "

        espacosResultado = ""
        qtdCaracteres = 32 - len(opcoes[opcoesRaj[i]])
        for c in range (0, qtdCaracteres):
            espacosResultado += " "

        print(opcoes[opcoesSheldon[i]] + espacos + opcoes[opcoesRaj[i]] + espacosResultado + resultado)






main()
