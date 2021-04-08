from random import randint
print('=-=' *10)
print('PAR OU ÍMPAR'.center(30))
print('=-=' *10)
cont = 0
while True:
    escolhapc = randint(0,10)
    escolhauser = int(input('Digite um número: '))
    parimpar = int(input('Digite 1 para par, ou 2 para ímpar: '))
    par = 0
    impar = 1
    if parimpar == 1:
        if (escolhauser + escolhapc) %2 == 0:
            print('-' * 20)
            print(f'Você jogou {escolhauser} e o computador {escolhapc}. Total de {escolhauser + escolhapc} DEU PAR')
            print('-' *20)
            print('Você venceu!')
            cont +=1
            print('Vamos jogar novamente...')
        elif (escolhauser + escolhapc) %2 == 1:
            print(f'Você jogou {escolhauser} e o computador {escolhapc}. Total {escolhauser + escolhapc} DEU ÍMPAR')
            print('Você perdeu!')
            break
    elif parimpar == 2:
        if (escolhauser + escolhapc) %2 == 1:
            print('-' * 20)
            print(f'Você jogou {escolhauser} e o computador {escolhapc}. Total {escolhauser + escolhapc} DEU ÍMPAR')
            print('-' * 20)
            print('Você venceu!')
            cont += 1
            print('Vamos jogar novamente...')
        elif (escolhauser + escolhapc) %2 == 0:
            print(f'Você escolheu {escolhauser} e o computador {escolhapc}. Total {escolhauser + escolhapc} DEU PAR')
            print('Você perdeu!')
            break
print(f'GAME OVER. Você venceu {cont} vezes!')