
class Info():
    def __init__(self):
        self.valores = []

    def getValores(self):
        return self.valores

    def inserirValores(self, n):
        self.valores.append(n)

filaValor = Info()
val = filaValor.getValores()
print(val)

filaValor.inserirValores("IESP")
filaValor.inserirValores("ED")
filaValor.inserirValores("2019.2")
filaValor.inserirValores("João Pessoa")
filaValor.inserirValores("Estágio 2")

print(val)



