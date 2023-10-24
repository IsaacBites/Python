vet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = []
impar = []

for i in vet:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print("Números pares:", par)
print("Números ímpares:", impar)
