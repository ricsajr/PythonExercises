from random import randint
v = 0
print('=-=' * 20)
print('Vamos jogar par ou ímpar!!!'.center(60))
print('=-=' * 20)
v = 0
while True:
    pc = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    escolha = ' '
    total = pc + jogador
    while escolha not in 'PI':
        escolha = str(input('Escolha PAR, ou ÍMPAR [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR') #operador ternário
    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER, você venceu {v} vezes!')
