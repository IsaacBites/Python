cont = 0
aux = 0
media = 0

while True:
    nota = float(input('Informe a sua nota'))
    opc = input('Você deseja inserir outra nota? (s - Sim, n - Não)')
    aux = aux + nota
    cont += 1
    
    if opc != 's':
        break

media = aux/cont

print(media)

 