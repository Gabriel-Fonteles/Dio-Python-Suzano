from datetime import datetime
menu = """ 
=======menu=======

  [1] Depositar
  [2] Sacar
  [3] Extrato
  [0] Sair
================== """

saldo = 0
limite = 1000
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
  
while True:
    
    opcao = input (menu)
    
    try:
        opcao = int(opcao)
    except ValueError:
        print("Opção selecionada é invalida!")
        continue
    
    #Deposito
    if opcao == 1:
        print ("====Depósito====")
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            data_hora = datetime.now() .strftime("%d-%m-%Y %H:%M:%S")
            extrato.append (f"Depósito: R$ {valor:.2f} em {data_hora}")
        else: 
            print("Operação Cancelada! O valor inserido é inválido.")
    
    #Saque
    
    elif opcao == 2:
        print ("====Saque====\n")
        valor = float(input("Qual valor vocÊ deseja sacar?\n"))
        
        excedeu_saldo = valor > saldo
        
        execedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação Cancelada! Você não tem saldo suficiente.")
        
        elif execedeu_limite:
            print("Operação Cancelada! o Valor excede o limite.")
            
        elif excedeu_saques:
            print("Operação Cancelada! Você atingiu a quantidade maxima de saques diarios.")
            
        elif valor > 0:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f} em {data_hora}")
            numero_saques += 1
            
        else:
            print("Operação Cancelada! O valor informado é invalido.")
            
    #Extrato
    elif opcao == 3:
        print("====Extrato====")
        if not extrato: # Se a lista extrato estiver vazia
            print("Não foram realizadas nenhuma movimentação.")
        else:
            for movimentacao in extrato: # Itera sobre cada item da lista extrato
                print(movimentacao)
        print(f"\nSaldo atual: R$ {saldo:.2f}") # Exibe o saldo no final do extrato
        print("=================")
        
    elif opcao == 0:
        break # Sai do loop
    
    else:
        print("Operação inválida, por favor selecione novamente uma opção válida.")