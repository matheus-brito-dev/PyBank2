''''
Projetinho básico de um banco em python
bootcamp engenheiro de dados - DIO
author: Matheus Brito de Oliveira
29/08/2024
saque,deposito e extrato, criar usuário, criar conta com validações propostas

'''

def listar_usuarios(usuarios):
    if not usuarios:
        print("Não há usuários cadastrados")
        return
        
    print("Listagem de Usuários".center(40,'#'))
    for usuario in usuarios:
        print(f"Usuário: {usuario['nome']} ")
        
def listar_contas(contas,usuarios):
    
    if not contas:
        print("Não há contas cadastradas.")
        return
          
    for conta in contas:
        for usuario in usuarios:
            if usuario['cpf'] == conta['usuario']:
                print(f"Conta número {conta['numero_conta']} e dono {usuario['nome']}")


def criar_conta(ag, contas, qtd_contas, usuarios):

    cpf = input("Informe seu cpf")

    if not usuarios:
        print("Lista de usuários está vazia.")
        return None, qtd_contas

    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

    if usuario is None:
        print("Usuário não cadastrado, favor criar um usuário primeiro")
        return None, qtd_contas

    qtd_contas += 1
    
    conta = {
        "agencia": ag,
        "numero_conta": qtd_contas,
        "usuario": usuario['cpf']
    }

    contas.append(conta)

    return conta, qtd_contas

def criar_usuario(usuarios):
    
    cpf = input("Informe seu cpf - DIGITE APENAS NÚMEROS")
  
    for usuario in usuarios:
        
        if usuario['cpf'] == cpf:
            print("Usuário já cadastrado")
            return
            
    nome = input("Informe seu nome")
    data_nascimento = input("Informe sua data de nascimento")
    logradouro = input("Informe seu endereço - Rua/Avenida")
    numero_logradouro = input("Informe o número da residência")
    bairro = input("Informe seu bairro")
    cidade = input("Informe a cidade - CIDADE/ESTADO")
    
    
    usuario = {
        
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "logradouro": logradouro,
        "numero_logradouro": numero_logradouro,
        "bairro": bairro,
        "cidade":cidade  
    } 
    usuarios.append(usuario)

    return usuario

def ver_extrato(saldo,*, extrato):
    print()
    print("EXTRATO".center(40,'#'))
    print()
    if extrato == "":
        print("Não foram realizadas movimentações")
    else:
        print(extrato)
    
    print(f'Seu saldo é R$ {saldo}\n')

def depositar(valor, saldo, extrato):
    if valor < 0.0:
        print("Para depositar, precisa ter algum valor")
    else:
        saldo += valor
        saida_operacao = f"(+) R$ {valor} DEPÓSITO\n"
        extrato += saida_operacao
            
    print(f'Seu saldo é R$ {saldo}')
    return saldo, extrato
    
def sacar(*, valor, saldo, limite, extrato, qtd_saque):
    if qtd_saque >= 3:
        print("Limite diário de saque ultrapassado")
    elif valor > saldo:
        print("Saldo insuficiente, por favor faça um depósito antes de sacar")
    elif valor > limite:
        print("Limite de saque ultrapassado, favor consultar o gerente")
    else:
        saldo -= valor
        saida_operacao = f"(-) R$ {valor} SAQUE\n"
        extrato += saida_operacao
        qtd_saque += 1
                
    print(f'Seu saldo é R$ {saldo}')
    return saldo, extrato, qtd_saque

def menu():
    decorator = '-'
    largura = 40
    titulo = "Bem vindo ao PyBank"
    print(f"{titulo.center(largura, decorator)}\n\n[1] - Criar Usuário\n[2] - Criar Conta\n[3] - Depositar\n[4] - Sacar\n[5] - Extrato\n[6] - Listar Contas\n[7] - Listar Usuários\n[8] - Sair")

def init(saldo, LIMITE, extrato):
    qtd_saque = 0
    qtd_contas =0
    usuarios = []
    contas = []
    AG = '001'
    menu()
    
    while True:
        op = int(input("Informe sua opção: "))
        
        if op == 1:
            usuario = criar_usuario(usuarios)
            print(f"Usuário {usuario['nome']} cadastrado com sucesso!")
        elif op == 2:
            conta, qtd_contas = criar_conta(AG,contas,qtd_contas,usuarios)
            if conta is not None:
                print(f"Conta criada com sucesso - o número da conta é {qtd_contas}")
        elif op == 3:
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)
        elif op == 4:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, qtd_saque = sacar(valor=valor, saldo=saldo, limite=LIMITE, extrato=extrato, qtd_saque=qtd_saque)
        elif op == 5:
            ver_extrato(saldo, extrato=extrato)
        elif op == 6:
            listar_contas(contas,usuarios)
        elif op ==7:
            listar_usuarios(usuarios)
        elif op ==8:
            print("O PyBank agradece sua visita, volte sempre!")
            break
        else:
            print("Opção inválida, por favor digite uma opção válida")

saldo = 0.0
extrato = ''
LIMITE = 500




init(saldo, LIMITE, extrato)
