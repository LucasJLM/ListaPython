jogador = {}
soma = 0
jogador['nome'] = str(input("Qual o nome: "))
jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou: "))

for c in range(jogador['partidas']) :
    gols = int(input(f"Quandos gols na partida {c}: "))
    
    soma += gols
    jogador['total_gols'] = soma

print('-='*30)

print(jogador)

print('-='*30)

for k,v in jogador.items() :
    print(f'O campo {k} tem o valor {v}')

print('-='*30)





