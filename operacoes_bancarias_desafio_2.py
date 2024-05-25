from datetime import datetime #imporação da função de data e hora

def menu(): #Menu de Opções com o nome do Banco
    print('*' * 30)
    print('U.R. MONEY BANK MENU'.center(30, '*'))
    print('*' * 30)
    print('''*       [1] - Saque          *
*       [2] - Extrato        *
*       [3] - Depósitar      *
*       [4] - Nova Conta     *
*       [5] - Listar Contas  *
*       [6] - Novo Usuário   *
*       [7] - Encerrar       *''')
    print('*' * 30)
    return input('Digite a opção desejada: ')

def saque(*, saldo, limite, extrato, numero_saques, limite_saques):
    print('Saque'.center(30))
    if numero_saques < limite_saques : #Verifica se o limite de saque foi excedido ao tentar realizar saque
        while True:
            saque = float(input('Digite o valor para o saque!\nR$ '))
            if saque <= saldo:
                if saque <= limite: 
                        print(f'Valor sacado R${saque:15.2f}')
                        saldo -= saque
                        data_hora = datetime.now() #variavel para receber a data e a hora
                        data_hora_formatada = data_hora.strftime('%d/%m/%Y %H:%M') #variável para receber e formatar a data e hora

                        extrato.append(f'{data_hora_formatada} - R${saque:.2f}')
                        
                        numero_saques += 1                        
                        break                        
                else:
                    print(f'Operação negada.\nSeu limite por saque é\nR$ {limite:.2f}\nLembrando de que você possui\n{limite_saques-numero_saques} saque(s) diario restante(s).')
                    break
            else:
                print('Saldo insuficiente para saque!')                    
                break
    else:
        print('Limite de saques diarios\nesgotado!\nEntre em contato com a\ngerência para mais\ninformações.') 
    return saldo, extrato, numero_saques

def imprime_extrato(saldo, /, *, extrato, saldo_anterior):
    print('Extrato'.center(30))
    print(f'Saldo Anterior R${saldo_anterior:13.2f}')

    for cont in range(0, len(extrato)): # cont contador auxiliar para percorrer a lista do extrato
        print(f'{extrato[cont]}'.rjust(30))
    else:
        print(f'Saldo Atual R${saldo:16.2f}')

def depositar(saldo, extrato, /):
    while True:
        valor = float(input('Digite o valor para depositar \nR$ '))
        if valor <= 0 :
            print('Valor para depósito inválido!')
            cancelar = input('Deseja depositar outro valor?\n[S/N] ').lower().strip()
            if cancelar in 'sn':
                if cancelar == 'n':
                    break
        else:                    
            saldo += valor
            data_hora = datetime.now()#variavel para receber a data e a hora
            data_hora_formatada = data_hora.strftime('%d/%m/%Y %H:%M')#variável para receber e formatar a data e hora
            extrato.append(f'{data_hora_formatada} + R${valor:.2f}')
            break 
    return saldo, extrato

def novo_usuario(usuarios):
    cpf = input('Digite o número do cpf.\n(Apenas números): ')
    usuario = pesquisa_usuario(cpf, usuarios)

    if usuario:
        print('Usuário já cadastrado')
        return
        
    nome = input('Digite o nome do usuário:\n')
    endereco = input('Digite o Endereço do usuário.\n(obs:. log, nº, cidade/uf):\n')
    data_nascimento = input('Data de Nascimento.\n(obs.: dd/mm/aaaa):\n')

    usuarios.append({'nome': nome, 'endereco':endereco, 'data_nascimento':data_nascimento, 'cpf':cpf})

def pesquisa_usuario(cpf, usuario):
    for valor in usuario:        
        if valor['cpf'] == cpf:
            return valor
    return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite o número do cpf.\n(Apenas números):')
    usuario = pesquisa_usuario(cpf, usuarios)

    if usuario:
        print('Conta Criada com Sucesso!'.center(30, '*'))
        return {'agencia': agencia, 'nro_conta': numero_conta, 'usuario':usuario}        
    print('Cliente não cadastrado.')

def listar_contas(contas):
    for conta in contas:
        print(f'Ag.: {conta["agencia"]} C/C.: {conta["nro_conta"]}\nTitular.: {conta["usuario"]["nome"]}')
        print('-'*30)
              
              
def main():
    LIMITE_SAQUE = 500
    NUMERO_SAQUE_DIARIO = 3
    AGENCIA = '0001'

    saldo = saldo_anterior = 500
    num_saques = 0
    extrato = []
    usuarios = []
    contas = []

    while True:        
        while True:
            operacao = menu()
            #operacao = input('Digite a opção desejada: ')
            if not operacao in ('1234567890'): # Verifica se as opções foram digitadas corretamente
                print(('Opção inválida').center(30,'*'))
                print(('Digite novamente!').center(30,'*'))            
            else:
                break

        print('*' * 30)

        match operacao: # Opções de Operações case 1 = Saque case 2 = Extrato case 3 = Depósito case 4 Encerrar
            case '1':
                saldo, extrato, num_saques = saque(saldo = saldo, 
                                                   limite = LIMITE_SAQUE, 
                                                   extrato = extrato, 
                                                   numero_saques = num_saques, 
                                                   limite_saques=NUMERO_SAQUE_DIARIO
                                                   )

            case '2':
                imprime_extrato(saldo, extrato=extrato, saldo_anterior=saldo_anterior)

            case '3':
                print('Depósitar'.center(30))                                
                saldo, extrato = depositar(saldo, extrato)

            case '4':
                print('Nova Conta'.center(30))
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)

            case '5':
                print('Listar Contas'.center(30))
                listar_contas(contas)
                                               
            case '6':
                print('Novo Usuário'.center(30))
                novo_usuario(usuarios)

            case '7':
                print('Volte sempre!'.center(30))
                print(('*' * 13).center(30))
                break
            case _:
                print('Opção inválida!')
main()
            

