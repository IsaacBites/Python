contador = 0
soma = 0

for _ in range (0, 6):
    x = float(input())

    if(x > 0):
        contador+=1
        soma = soma + x

print(contador, 'valores positivos' )
print(soma/contador)