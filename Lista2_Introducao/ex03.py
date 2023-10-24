import random

num = random.randint(1, 100)

while True:
    opc = int(input('CHute um número: '))
    if opc < num:
        print('O número chutado é muito baixo')
    elif opc > num:
        print('O número chutado é muito alto')
    else:
        print('Você acertou o número')
        break