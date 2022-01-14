def maior_elemento(lista):
    maior = 0
    
    for k in range(len(lista)):
        lista[k] = int(lista[k])
    
    for i in range(len(lista)):
        if lista[i] > maior or i == 0:
            maior = lista[i]
            
    return maior

lista = input().split()

print(maior_elemento(lista))