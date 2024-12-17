from time import sleep
def contador(i,f,p) :
    print('-'*20)
    print(f'Contagem de {i} até {f} pulando {p} números')
    print('-'*20)

    for c in range(0,11):
       
        print(c,end=' ')
        sleep(1)
        

contador(1,10,1)