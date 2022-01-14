def soma_elementos(lista):
    for k in range(len(lista)):
        lista[k] = int(lista[k])
    
    soma = 0
    
    for i in range(len(lista)):
        soma += lista[i]
            
    return soma

lista = input().split()

print(soma_elementos(lista))