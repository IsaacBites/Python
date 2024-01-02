vertebrado = input()
Tipo = input()
Alimentacao = input()

if vertebrado == 'vertebrado':
    if Tipo == 'ave':
        if Alimentacao == 'carnivoro':
            print('aguia')
        if Alimentacao == 'onivoro':
            print('pomba')
    if Tipo == 'mamifero':
        if Alimentacao == 'onivoro':
            print('homem')
        if Alimentacao == 'herbivoro':
            print('vaca')        
elif vertebrado == 'invertebrado':
    if Tipo == 'inseto':
        if Alimentacao == 'hematofago':
            print('pulga')
        if Alimentacao == 'herbivoro':
            print('lagarta')
    if Tipo == 'anelideo':
        if Alimentacao == 'hematofoto':
            print('sanguessuga')
        if Alimentacao == 'onivoro':
            print('minhoca')  
else:
    print('Inválido')