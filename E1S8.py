def remove_repetidos(lista):
    for k in range(len(lista)):
        lista[k] = int(lista[k])
    
    lista = sorted(lista)
    
    lst = []
    
    for i in range(len(lista)):
        if lista[i] not in lst:
            lst.append(lista[i])
            
    return lst

lista = input().split()

print(remove_repetidos(lista))