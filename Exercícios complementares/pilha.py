class Pilha():

    def __init__(self):
        self.letras = []

    def getPilha(self):
        return self.letras

    def inserirLetras(self, novaLetra):
        self.letras.append(novaLetra)


def main():

    pilhaVar = Pilha()

    caracteres = str (input ("Quais caracteres você deseja inserir: "))
    for i in (caracteres):
        pilhaVar.inserirLetras(i)

        print(pilhaVar.getPilha())

main()