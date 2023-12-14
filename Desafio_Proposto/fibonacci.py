def fibo(n):            
    sequencia = [0, 1] 
    for i in range(2, n):  
        soma = sequencia[-1] + sequencia[-2]   
        sequencia.append(soma)
    return sequencia   

n = int(input("Digite o número: "))  

if n <= 0:                                                        
    print("Número inválido")  
else:
    sequ = fibo(n)
    print(sequ)