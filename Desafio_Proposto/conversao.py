def convertendo(horas, minutos):

    periodo = 'A.M.' if 0 <= horas < 12 else 'P.M.'
    
    if horas == 0:
        horas = 12
    elif horas > 12:
        horas -= 12    
    
    return horas, minutos, periodo  

def resultado(horas, minutos, periodo):  
    print(f"Horas: {horas}:{minutos} {periodo}") 


while True:
    horas = int(input("Digite a hora: "))      
    minutos = int(input("Digite os minutos: ")) 

    if 0 <= horas <= 23 and 0 <= minutos <= 59:  
 
        hora_nova, minute_novo, periodo_novo = convertendo(horas, minutos)
        resultado(hora_nova, minute_novo, periodo_novo) 
    else:
        print("Numero inválido") 

    x = input("Quer continuar? (S - Sim, N - Qualquer outra letra):").upper() 
    if x != 'S':   
        break
