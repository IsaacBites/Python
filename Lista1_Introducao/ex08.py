num = int(input('Informe o números de elementos na lista: '))
vet = []
soma = 0
for i in range(1, num + 1):
    val = int(input("Informe os valores da lista"))
    vet.append(val)
    soma = soma + val

print(vet)
print(soma)

