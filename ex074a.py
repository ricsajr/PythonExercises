from random import randint
tup = tuple(randint(0, 10) for i in range(0, 5))#especificar o tipo de coleção antes da abertura de parênteses para executar ação dentro da coleção
print(f'Os números escolhidos randomicamente foram {tup}; sendo o maior {max(tup)} e o menor {min(tup)}')