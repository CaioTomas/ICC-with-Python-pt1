def éPrimo(x):
    fator = 2
    while x%fator != 0 and fator <= x**(1/2):
        fator += 1
    if x%fator == 0:
        return False
    else:
        return True
    
def n_primos(x):
    quant = 0
    for i in range(1,x+1):
        if éPrimo(i):
            quant += 1
    return quant

n = int(input().split()[0])

print(n_primos(n))