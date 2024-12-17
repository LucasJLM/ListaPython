lista_completa = []
lista_par = []
lista_impar = []

while True : 
    valores = int(input("Digite   valor: "))
    lista_completa.append(valores)

    if valores % 2 == 0 :
        lista_par.append(valores)
    else :
        lista_impar.append(valores)
        

    
    resposta = str(input("Você deseja continuar? [ S ]/[ N ]"))

    if resposta in 'Nn':
        break
print('-='*20)
print(f'Essa é a sua lista: {lista_completa}')
print(f'Essa é a lista somente com os pares: {lista_par}')
print(f'Essa é a lista somente com os Impares: {lista_impar}')