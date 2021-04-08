listaTimes = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo',
          'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Atlético-PR',
          'Bragantino', 'Ceará-SC', 'Corinthians', 'Atlético-GO', 'Bahia',
          'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba',
          'Botafogo')
print('Os 5 primeiros são:')
for cont, time in enumerate(listaTimes[:5]): #para utilizar a pos 1 como contador, preciso utilizar o enumerate
    print(f'{cont + 1}° {time}')