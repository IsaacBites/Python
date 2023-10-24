opc = int(input('Informe para qual moeda você deseja fazer a conversão? (1 - dollar, 2 - euro): '))
valor = float(input('Informe o seu saldo em R$: '))

if opc == 1:
    valor = valor * 5.0
else: 
    valor = valor * 5.26
print(valor)