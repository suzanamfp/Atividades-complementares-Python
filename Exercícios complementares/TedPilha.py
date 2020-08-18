
def testaMaisElementos(p1, p2):
    #p1.getPilha ()
   #p2.getPilha ()
    if p1.getPilha() > p2.getPilha():
        return 1

    return 0

class Pilha():
    def __init__(self):
        self.pilha = []


    def getPilha(self):
        return self.pilha

    def inserirValores(self, novoValor):
        self.pilha.append(novoValor)



def main():

     p1 = Pilha()
     p2 = Pilha()

     valoresP1 = str (input ("Quais valores você deseja inserir na pilha 1: "))
     for i in (valoresP1):
         p1.inserirValores(i)
         print(p1.getPilha())

     valoresP2 = str (input ("Quais valores você deseja inserir na pilha 2: "))
     for i in (valoresP2):
        p2.inserirValores (i)
        print(p2.getPilha ())

     if testaMaisElementos(p1,p2) == True:
         print("Verdadeiro")
     else:
         print("Falso")


main()


