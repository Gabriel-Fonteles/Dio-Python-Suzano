MAIOR_IDADE = 18


idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
    
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")
    
##Aninhado
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizao com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, slado insuficiente!")

elif conta_universitaria:
    
    if saldo >= saque:
        print("Saque relaizado com sucesso!")
    else:
        print("Saldo insuficiente!")

else:
    print("Sistema não reconhecey seu tipo de conta, entre em contato com seu gerente")
    
#ternaria
saldo = 2000
saque = 500

status = "Secesso" if saldo >= saque else "Falha"

print (f"{status} ao realizar o saque!")