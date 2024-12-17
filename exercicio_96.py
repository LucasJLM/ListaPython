def area(b,h) :
    
    calculo = b*h
    
    print('-'*30)
    print(f'A área de um terreno {b} x {h} é igual a  : {calculo}m')
    print('-'*30)


b = float(input("Qual a base desse poligono: "))
h= float(input("Qual a altura desse poligono:"))

area(b,h) 