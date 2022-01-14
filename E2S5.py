def eprimo(n):
    cont = 1
    div = 0

    while cont <= n:
        if n%cont == 0:
            div += 1
        cont += 1

    if div == 2:
        return True
    else:
        return False

def maior_primo(n):
    i = 0
    maior = 2

    for i in range(n+1):
        if eprimo(i):
            maior = i
    return maior

num = int(input())

print(maior_primo(num))