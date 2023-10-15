#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em um lista. No final, mostre:
#a)Quantas pessoas foram cadastradas
#b)A média de idade do grupo
#c)Uma lista com todas as mulheres
#d)Uma lista com todas as pessoas com idade acima da média

galera = list()
pessoa = dict()
soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro de digitação. Por favor, digite M ou F ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro de digitação. Por favor, responde S ou N')
    if resp == 'N':
        break

print(f'a) Ao todo temos {len(galera)} pessoas cadastradas')

media = soma / len(galera)

print(f'b) A média de idade é {media:.2f} anos')

print('c) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')

print('\nd) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')