def cadastrarCliente(agenda):


    nome = str(input('Nome: '))

    if nome == "" :
        print("Digite um nome válido!")
        return 0


    atributos = {}
    atributos['debito']   = float(input('Débito: '))
    atributos['telefone'] = str  (input('Telefone: ' ))
    atributos['endereco'] = str  (input('Endereço: ' ))

    agenda[nome] = atributos

    print("Cadastro de Cliente")
    print(agenda[nome])


def atualizarValores(agenda):

    print("Atualização dos valores em dívida")

    cliente = str(input("Digite o nome do cliente: "))

    if cliente in agenda.keys() :
        novoDebito = float (input ("Digite o valor do novo débito: "))
        valorPago = float (input ('Digite o valor que o cliente pagou:'))
        agenda[cliente]['debito'] = agenda[cliente]['debito'] - valorPago + novoDebito
        print(agenda[cliente]['debito'])
        if agenda[cliente]['debito'] == 0:
            print("Cliente sem débito!")
    else :
        print ("Cliente não Existe!")



def removerCliente(agenda):
    print ("Remover Cliente")

    keysDelete = []
    for chave in agenda.keys() :
        if agenda[chave]['debito'] == 0 :
            keysDelete.append(chave)

    for i in range(0,len(keysDelete)):
        del(agenda[keysDelete[i]])

    print(agenda)


def buscarCliente(agenda):
    print ("Buscar Cliente")

    cliente = str (input ("Digite o nome do cliente você deseja buscar:"))
    if cliente in agenda.keys() :
        print(agenda[cliente])

def menu (agenda):

    while (True):
        print("Menu: ")

        print ("1. Cadastrar cliente")
        print ("2. Atualizar dívida")
        print ("3. Remover cliente")
        print ("4. Buscar cliente")
        print ("0. Sair")


        opcao = input ("O que você deseja fazer?")

        if opcao == "1":
            cadastrarCliente(agenda)
            print ("Cliente cadastrado com sucesso!")
        elif opcao == "2":
            atualizarValores(agenda)
            print ("Débito atualizados!")
        elif opcao == "3":
            removerCliente(agenda)
            print ("Cliente removido com sucesso!")
        elif opcao == "4":
            buscarCliente(agenda)
            print("Busca realizada com sucesso!")
        elif opcao == "0":
            print ("sair!")
            break




def main():

    agenda = {}
    menu(agenda)

main()






