vet = []
x = int(input('Informe a quantidade de números que deseja colocar na lista?: '))

for i in range(1, x + 1):
    val = int(input('Insira os valores da lista: '))
    vet.append(val)
    vet.sort()

print(vet)
    