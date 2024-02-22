contador = 0

for _ in range (0, 5):
    x = float(input())

    if(x % 2 == 0):
        contador+=1

print(contador, 'valores pares' )
