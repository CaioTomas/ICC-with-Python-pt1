n = int(input('Digite um número inteiro: '))

cont = 1
div = 0

while cont <= n:
    if n%cont == 0:
        div += 1
    cont += 1

if div == 2:
    print('primo')
else:
    print('não primo')