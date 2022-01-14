def é_hipotenusa(n):
    i = 1
    cont = 0
    while i <= n-1:
        j = 1
        while j <= n-1:
            soma_quadrados = i**2 + j**2
            if n**2 == soma_quadrados:
                cont = 1
                j = n
            else:
                j += 1
        i += 1
    if cont == 1:
        return True
    else:
        return False
    
def soma_hipotenusas(n):
    soma = 0
    for i in range(1,n+1):
        if é_hipotenusa(i):
            soma += i
    return soma
    

num = int(input().split()[0])
print(soma_hipotenusas(num))