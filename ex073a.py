serieA = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo',
          'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Atlético-PR',
          'Bragantino', 'Ceará-SC', 'Corinthians', 'Atlético-GO', 'Bahia',
          'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba',
          'Botafogo')

def linha():
    print('=-=' * 10)

print('TABELA SÉRIE A')
linha()
print('Os 5 primeiros são:')
for cont, time in enumerate(serieA[:5]): #para utilizar a pos 1 como contador, preciso utilizar o enumerate
    print(f'{cont + 1}° {time}')
linha()
print(f'Os 17°, 18°, 19° e 20° últimos colocados são:{serieA[-4:]}')
linha()
print(f'Os 20 primeiros em ordem alfabética seriam> {sorted(serieA)}')
linha()
posFortaleza = serieA.index('Fortaleza')+1
print(f'O Fortaleza se encontra na {posFortaleza}° posição')


