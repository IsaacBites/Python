contadorPar = 0
contadorImpar = 0
contadorPositivo = 0
contadorNegativo = 0


for _ in range(0, 5):
    x = float(input())

    if(x % 2 == 0):
        contadorPar+=1
    else:
        contadorImpar+=1

    if(x > 0):
        contadorPositivo+=1
    elif(x < 0):
        contadorNegativo+=1


print(f"{contadorPar} valor(es) par(es)")
print(f"{contadorImpar} valor(es) impar(es)")
print(f"{contadorPositivo} valor(es) positivo(s)")
print(f"{contadorNegativo} valor(es) negativo(s)")