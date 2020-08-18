def main():

    pesoMetab = float(input("Digite o peso do animal: "))
    k = int(input("Digite o valor correspondente a espécie pela tabela:"))

    if (k ==129) :
         print ("Grupo1 - Passeriformes")
    elif (k == 78):
        print("Grupo2 - Não Passeriformes")
    elif (k == 70):
        print("Grupo3 - Mamíferos Placentários")
    elif (k == 49):
        print("Grupo4 - Marsupiais e Edentatas")
    elif (k == 10):
        print("Grupo5 - Répteis")

    calTaxaMetab = (pesoMetab**0.75) * k
    print ("A taxa metabólica do animal é: ", calTaxaMetab)


main()