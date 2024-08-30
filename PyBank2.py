{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "3077af46-667f-49ea-9203-dc4069a27d97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "----------Bem vindo ao PyBank-----------\n",
      "\n",
      "[1] - Criar Usuário\n",
      "[2] - Criar Conta\n",
      "[3] - Depositar\n",
      "[4] - Sacar\n",
      "[5] - Extrato\n",
      "[6] - Listar Contas\n",
      "[7] - Listar Usuários\n",
      "[8] - Sair\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Informe sua opção:  1\n",
      "Informe seu cpf - DIGITE APENAS NÚMEROS 123\n",
      "Informe seu nome RERERE\n",
      "Informe sua data de nascimento RERERE\n",
      "Informe seu endereço - Rua/Avenida RERER\n",
      "Informe o número da residência RERER\n",
      "Informe seu bairro RERE\n",
      "Informe a cidade - CIDADE/ESTADO RERE\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Usuário RERERE cadastrado com sucesso!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Informe sua opção:  2\n",
      "Informe seu cpf 123\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Conta criada com sucesso - o número da conta é 1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Informe sua opção:  3\n",
      "Informe o valor do depósito:  1000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Seu saldo é R$ 1000.0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Informe sua opção:  4\n",
      "Informe o valor do saque:  100\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Seu saldo é R$ 900.0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Informe sua opção:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "################EXTRATO#################\n",
      "\n",
      "(+) R$ 1000.0 DEPÓSITO\n",
      "(-) R$ 100.0 SAQUE\n",
      "\n",
      "Seu saldo é R$ 900.0\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Informe sua opção:  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "##########Listagem de Usuários##########\n",
      "Usuário: RERERE \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Informe sua opção:  8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "O PyBank agradece sua visita, volte sempre!\n"
     ]
    }
   ],
   "source": [
    "''''\n",
    "Projetinho básico de um banco em python\n",
    "bootcamp engenheiro de dados - DIO\n",
    "author: Matheus Brito de Oliveira\n",
    "29/08/2024\n",
    "saque,deposito e extrato, criar usuário, criar conta com validações propostas\n",
    "\n",
    "'''\n",
    "\n",
    "def listar_usuarios(usuarios):\n",
    "    if not usuarios:\n",
    "        print(\"Não há usuários cadastrados\")\n",
    "        return\n",
    "        \n",
    "    print(\"Listagem de Usuários\".center(40,'#'))\n",
    "    for usuario in usuarios:\n",
    "        print(f\"Usuário: {usuario['nome']} \")\n",
    "        \n",
    "def listar_contas(contas,usuarios):\n",
    "    \n",
    "    if not contas:\n",
    "        print(\"Não há contas cadastradas.\")\n",
    "        return\n",
    "          \n",
    "    for conta in contas:\n",
    "        for usuario in usuarios:\n",
    "            if usuario['cpf'] == conta['usuario']:\n",
    "                print(f\"Conta número {conta['numero_conta']} e dono {usuario['nome']}\")\n",
    "\n",
    "\n",
    "def criar_conta(ag, contas, qtd_contas, usuarios):\n",
    "\n",
    "    cpf = input(\"Informe seu cpf\")\n",
    "\n",
    "    if not usuarios:\n",
    "        print(\"Lista de usuários está vazia.\")\n",
    "        return None, qtd_contas\n",
    "\n",
    "    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)\n",
    "\n",
    "    if usuario is None:\n",
    "        print(\"Usuário não cadastrado, favor criar um usuário primeiro\")\n",
    "        return None, qtd_contas\n",
    "\n",
    "    qtd_contas += 1\n",
    "    \n",
    "    conta = {\n",
    "        \"agencia\": ag,\n",
    "        \"numero_conta\": qtd_contas,\n",
    "        \"usuario\": usuario['cpf']\n",
    "    }\n",
    "\n",
    "    contas.append(conta)\n",
    "\n",
    "    return conta, qtd_contas\n",
    "\n",
    "def criar_usuario(usuarios):\n",
    "    \n",
    "    cpf = input(\"Informe seu cpf - DIGITE APENAS NÚMEROS\")\n",
    "  \n",
    "    for usuario in usuarios:\n",
    "        \n",
    "        if usuario['cpf'] == cpf:\n",
    "            print(\"Usuário já cadastrado\")\n",
    "            return\n",
    "            \n",
    "    nome = input(\"Informe seu nome\")\n",
    "    data_nascimento = input(\"Informe sua data de nascimento\")\n",
    "    logradouro = input(\"Informe seu endereço - Rua/Avenida\")\n",
    "    numero_logradouro = input(\"Informe o número da residência\")\n",
    "    bairro = input(\"Informe seu bairro\")\n",
    "    cidade = input(\"Informe a cidade - CIDADE/ESTADO\")\n",
    "    \n",
    "    \n",
    "    usuario = {\n",
    "        \n",
    "        \"nome\": nome,\n",
    "        \"data_nascimento\": data_nascimento,\n",
    "        \"cpf\": cpf,\n",
    "        \"logradouro\": logradouro,\n",
    "        \"numero_logradouro\": numero_logradouro,\n",
    "        \"bairro\": bairro,\n",
    "        \"cidade\":cidade  \n",
    "    } \n",
    "    usuarios.append(usuario)\n",
    "\n",
    "    return usuario\n",
    "\n",
    "def ver_extrato(saldo,*, extrato):\n",
    "    print()\n",
    "    print(\"EXTRATO\".center(40,'#'))\n",
    "    print()\n",
    "    if extrato == \"\":\n",
    "        print(\"Não foram realizadas movimentações\")\n",
    "    else:\n",
    "        print(extrato)\n",
    "    \n",
    "    print(f'Seu saldo é R$ {saldo}\\n')\n",
    "\n",
    "def depositar(valor, saldo, extrato):\n",
    "    if valor < 0.0:\n",
    "        print(\"Para depositar, precisa ter algum valor\")\n",
    "    else:\n",
    "        saldo += valor\n",
    "        saida_operacao = f\"(+) R$ {valor} DEPÓSITO\\n\"\n",
    "        extrato += saida_operacao\n",
    "            \n",
    "    print(f'Seu saldo é R$ {saldo}')\n",
    "    return saldo, extrato\n",
    "    \n",
    "def sacar(*, valor, saldo, limite, extrato, qtd_saque):\n",
    "    if qtd_saque >= 3:\n",
    "        print(\"Limite diário de saque ultrapassado\")\n",
    "    elif valor > saldo:\n",
    "        print(\"Saldo insuficiente, por favor faça um depósito antes de sacar\")\n",
    "    elif valor > limite:\n",
    "        print(\"Limite de saque ultrapassado, favor consultar o gerente\")\n",
    "    else:\n",
    "        saldo -= valor\n",
    "        saida_operacao = f\"(-) R$ {valor} SAQUE\\n\"\n",
    "        extrato += saida_operacao\n",
    "        qtd_saque += 1\n",
    "                \n",
    "    print(f'Seu saldo é R$ {saldo}')\n",
    "    return saldo, extrato, qtd_saque\n",
    "\n",
    "def menu():\n",
    "    decorator = '-'\n",
    "    largura = 40\n",
    "    titulo = \"Bem vindo ao PyBank\"\n",
    "    print(f\"{titulo.center(largura, decorator)}\\n\\n[1] - Criar Usuário\\n[2] - Criar Conta\\n[3] - Depositar\\n[4] - Sacar\\n[5] - Extrato\\n[6] - Listar Contas\\n[7] - Listar Usuários\\n[8] - Sair\")\n",
    "\n",
    "def init(saldo, LIMITE, extrato):\n",
    "    qtd_saque = 0\n",
    "    qtd_contas =0\n",
    "    usuarios = []\n",
    "    contas = []\n",
    "    AG = '001'\n",
    "    menu()\n",
    "    \n",
    "    while True:\n",
    "        op = int(input(\"Informe sua opção: \"))\n",
    "        \n",
    "        if op == 1:\n",
    "            usuario = criar_usuario(usuarios)\n",
    "            print(f\"Usuário {usuario['nome']} cadastrado com sucesso!\")\n",
    "        elif op == 2:\n",
    "            conta, qtd_contas = criar_conta(AG,contas,qtd_contas,usuarios)\n",
    "            if conta is not None:\n",
    "                print(f\"Conta criada com sucesso - o número da conta é {qtd_contas}\")\n",
    "        elif op == 3:\n",
    "            valor = float(input(\"Informe o valor do depósito: \"))\n",
    "            saldo, extrato = depositar(valor, saldo, extrato)\n",
    "        elif op == 4:\n",
    "            valor = float(input(\"Informe o valor do saque: \"))\n",
    "            saldo, extrato, qtd_saque = sacar(valor=valor, saldo=saldo, limite=LIMITE, extrato=extrato, qtd_saque=qtd_saque)\n",
    "        elif op == 5:\n",
    "            ver_extrato(saldo, extrato=extrato)\n",
    "        elif op == 6:\n",
    "            listar_contas(contas,usuarios)\n",
    "        elif op ==7:\n",
    "            listar_usuarios(usuarios)\n",
    "        elif op ==8:\n",
    "            print(\"O PyBank agradece sua visita, volte sempre!\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Opção inválida, por favor digite uma opção válida\")\n",
    "\n",
    "saldo = 0.0\n",
    "extrato = ''\n",
    "LIMITE = 500\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "init(saldo, LIMITE, extrato)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24813e69-c13b-43e9-bb98-6aa0a3935acf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
