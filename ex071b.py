valor = int(input('Quanto deseja sacar? '))
m = q1 = q10 = q20 = q50 = 0
m = valor
while m - 50 > 0:
    q50 += 1
    m -= 50
while m - 20 > 0:
    q20 += 1
    m -= 20
while m - 10 > 0:
    q10 += 1
    m -= 10
while m - 1 >= 0:
    q1 += 1
    m -= 1

print(q50, q20, q10, q1)