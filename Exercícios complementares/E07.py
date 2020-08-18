def main():
    valorHora = int(input('Digit o valor da hora trabalhada:'))
    horasTrabalhadas = int(input('Digite a quantidade de horas trablhada:'))

    salarioBruto = valorHora*horasTrabalhadas
    custoIPRE = valorHora*horasTrabalhadas * 0.11
    custoINSS = valorHora * horasTrabalhadas * 0.08
    custoSindicato = valorHora*horasTrabalhadas* 0.05
    salarioLiq = salarioBruto - (custoIPRE+custoINSS+custoSindicato)
    custoDesc = (custoIPRE+custoSindicato+custoINSS)

    print(salarioBruto)
    print(custoIPRE)
    print(custoINSS)
    print(custoSindicato)
    print(salarioLiq)
    print(custoDesc)


main()
