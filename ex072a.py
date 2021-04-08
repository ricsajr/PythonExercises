numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte' )
aux = 'Ss'
while True:
        if aux not in 'Ss':
            break
        while True:
            user = int(input('Digite um número entre 0 e 20 para lê-lo por extenso: '))
            if 0 <= user <=20:
                break
            print('Tente novamente. ', end='')
        print(f'O numero digitado foi {user}. Por extenso é: {numeros[user]}')
        while True:
            aux = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
            if aux in 'SsNn':
                break

