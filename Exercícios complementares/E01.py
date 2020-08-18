import math
print("------TINTAS------")

Area= float(input('Digite o tamanho da área:'))
ValorLata= float(input('Digite o valor da lata de tinta:'))

QuantTintas = Area /3
print('A quantidade de tintas que você precisará será de: {}L'.format(QuantTintas))

#Litos = 18L por lata

QuantLatas = math.ceil(QuantTintas/18)

print('Quantidade de latas: {}'.format(QuantLatas))


PrecoFinal = QuantLatas * ValorLata
print('O valor final é de: {}'. format(PrecoFinal))

