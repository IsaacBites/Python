sal = float(input())

if 0 <= sal <= 400:
    reajuste = sal + (sal * 0.15)
    print(f"Novo salario: {reajuste:.2f}")
    print(f"Reajuste ganho: {sal * 0.15:.2f}")
    print('Em percentual: 15 %')
elif 400.01 <= sal <= 800:
    reajuste = sal + (sal * 0.12)
    print(f"Novo salario: {reajuste:.2f}")
    print(f"Reajuste ganho: {sal * 0.12:.2f}")
    print('Em percentual: 12 %')
elif 800.01 <= sal <= 1200:
    reajuste = sal + (sal * 0.1)
    print(f"Novo salario: {reajuste:.2f}")
    print(f"Reajuste ganho: {sal * 0.1:.2f}")
    print('Em percentual: 10 %')
elif 1200.01 <= sal <= 2000:
    reajuste = sal + (sal * 0.07)
    print(f"Novo salario: {reajuste:.2f}")
    print(f"Reajuste ganho: {sal * 0.07:.2f}")
    print('Em percentual: 7 %')
else:
    reajuste = sal + (sal * 0.04)
    print(f"Novo salario: {reajuste:.2f}")
    print(f"Reajuste ganho: {sal * 0.04:.2f}")
    print('Em percentual: 4 %')