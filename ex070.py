valorFinal = maisDeMil = precoIgual = 0
produto = str(input("Digite o nome do produto: "))
preco = float(input("Digite o preço do produto; R$: "))
nomeMenor = produto
precoMenor = preco
valorFinal += preco
if preco > 1000:
    maisDeMil += 1
decide = str(input('Deseja continuar? [S/N]: ')).strip()[0].upper()
while decide not in 'N':
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto; R$: "))
    valorFinal += preco
    if preco < precoMenor:
        precoIgual = 0
        precoMenor = preco
        nomeMenor = produto
    elif preco == precoMenor:
        precoIgual += 1
    if preco > 1000:
        maisDeMil += 1
    decide = str(input("Deseja continuar? [S/N]: ")).strip()[0].upper()
print(f'''VALOR FINAL DA COMPRA: R$: {valorFinal}
PRODUTO MAIS BARATO: {nomeMenor}. HÁ OUTROS {precoIgual} produtos de mesmo valor (R$: {precoMenor})
PRODUTOS ACIME DE R$: 1000,00: {maisDeMil}''')

