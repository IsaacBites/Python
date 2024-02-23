x = int(input())

if 1 <= x <= 1000:
    vet = []
    for i in range(1, x, 2):
        vet.append(i)
    print(vet)
else:
    print("invalido")