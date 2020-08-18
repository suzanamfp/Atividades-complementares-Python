
class Fila():
    def __init__(self):
        self.valores = [-1, -2, -3, -4]

    def getValores(self):
        return self.valores

filaValor = Fila()
val = filaValor.getValores()
print(val)
