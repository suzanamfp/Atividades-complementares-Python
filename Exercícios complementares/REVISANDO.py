
quantNum = int(input("Quantos números você quer digitar: "))
quantNeg = 0
while(quantNum != 0):
    numeros = int(input("Digite um número: "))
    quantNum = quantNum - 1
    if (numeros < 0):
        quantNeg = quantNeg + 1

        print(quantNeg)
        print (numeros)













