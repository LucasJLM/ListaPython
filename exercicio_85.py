lista_completa = [[],[]]
valor = 0

for c in range(0,7):
    valor = int(input("Digite um valor: "))

    if valor % 2 == 0 :
        lista_completa[0].append(valor)
       

    else :
        lista_completa[1].append(valor)
        

lista_completa[0].sort()
lista_completa[1].sort()

print(lista_completa)