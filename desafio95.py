#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento do jogador

#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('Erro de digitação. Digite S/N')
    if resp == 'N':
        break
for i, j in enumerate(time):
    print(f'{k}', end='')
    for d in v.values():
        


print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')

for i, v in enumerate(jogador['Gols']):
    print(f' - Na partida {i+1}, fez {v} gols')

print(f'Foi um total de {jogador["Total"]} gols')