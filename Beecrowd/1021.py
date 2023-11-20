valor = float(input())

#cédulas

int100 = int(valor // 100)
valor %= 100

int50 = int(valor // 50)
valor %= 50

int20 = int(valor // 20)
valor %= 20

int10 = int(valor // 10)
valor %= 10

int5 = int(valor // 5)
valor %= 5

int2 = int(valor // 2)
valor %= 2

#Moedas

int01 =int(valor // 1)
valor %= 1

int050 = int(valor // 0.5)
valor %= 0.5

int025 = int(valor // 0.25)
valor %= 0.25

int010 = int(valor // 0.1)
valor %= 0.1

int05 = int(valor // 0.05)
valor %= 0.05

int001 = int(valor // 0.01)


print('NOTAS:')
print(f"{int100} nota(s) de R$ 100.00")
print(f"{int50} nota(s) de R$ 50.00")
print(f"{int20} nota(s) de R$ 20.00")
print(f"{int10} nota(s) de R$ 10.00")
print(f"{int5} nota(s) de R$ 5.00")
print(f"{int2} nota(s) de R$ 2.00")
print('MOEDAS:')
print(f"{int01} moeda(s) de R$ 1.00")
print(f"{int050} moeda(s) de R$ 0.50")
print(f"{int025} moeda(s) de R$ 0.25")
print(f"{int010} moeda(s) de R$ 0.10")
print(f"{int05} moeda(s) de R$ 0.05")
print(f"{int001} moeda(s) de R$ 0.01")