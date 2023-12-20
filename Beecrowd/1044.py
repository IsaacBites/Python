num1 = int(input())
num2 = int(input())

resto = num2 % num1

if num1 % num2 == 0 or num2 % num1 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')