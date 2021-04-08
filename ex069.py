print("CADASTRAMENTO")
somaIdade = totalHomens = mulheres20 = 0
while True:
    sexo = int(input("Informe seu sexo:\n[ 1 ] FEMININO\n[ 2 ] MASCULINO\n[ 3 ] OUTRO\n[ 0 ] SAIR\nSua escolha: "))
    if sexo == 0:
        break
    idade = int(input("Digite sua idade: "))
    if idade > 18:
            somaIdade = somaIdade + 1
    if sexo == 2:
            totalHomens += 1
    elif sexo == 1 and idade < 20:
        mulheres20 += 1


    continuar = str(input('deseja continuar o cadastro? [S/N]:  ').upper().strip())
    if continuar == "N":
        break

print(f'''Ao todo foram cadastrados(as): {mulheres20} mulheres com menos de 20 anos
                               {totalHomens} Homens
                               {somaIdade} pessoas com mais de 18 anos''')
