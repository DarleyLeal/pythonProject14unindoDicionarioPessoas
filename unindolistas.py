# Exercicio de Python - Lista / Dicionário com pessoas e idades

pessoas = dict()
lista_pessoas = list()
cont = soma = 0
while True:
    pessoas['nome'] = input('Nome: ').capitalize().strip()
    cont += 1
    while True: #laço se repete até o usuário digite f ou m
        pessoas['sexo'] = input('Sexo: M/F').upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro, tente apenas M ou F')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista_pessoas.append(pessoas.copy())
    while True: #laço se repete até que seja digitado s ou n
        opc = input('Deseja cadastrar mais pessoas? S/N').upper().strip()[0]
        if opc in 'NS':
            break
        print('Digite apenas S ou N para continuar ')
    if opc in 'S':
        continue # laço volta ao inicio e adiciona mais pessoas
    else:
        break
# Programa Principal
print('=' * 30)
print(f'{cont} pessoas foram cadastradas.') # Conta quantas pessoas foram cadastradas
print('=' * 30)
media = (soma / cont)
print(f'A média de idade é: {media:.0f} anos')
print('=' * 40)
for i in lista_pessoas:
    if i['idade'] >= media:
        print(f'Lista de pessoas com idade acima da média: {i["nome"]}')
print('=' * 40)
for i in lista_pessoas:
    if i['idade'] < media:
        print(f'Lista de pessoas com idade a baixo da média: {i["nome"]}')
print('=' * 40)
for p in lista_pessoas:
    if p['sexo'] in 'Ff':
        print(f'Lista de Mulheres: {p["nome"]}')
for p in lista_pessoas:
    if p['sexo'] in 'Mm':
        print(f'Lista de Homens na lista: {p["nome"]}')
