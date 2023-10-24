while True:
    n = int(input('Digite um numero: '))
    fatorial = 1

    for i in range(1, n + 1):
        fatorial = fatorial * i
    
    print(fatorial)

    opc = int(input('Deseja continuar?(1 - Não, 2 - Sim):'))
    if opc == 1:
        break

print('Processo finalizado')