largura = int(input('digite a largura: ').split()[0])
altura = int(input('digite a altura: ').split()[0])

for i in range(altura):
    if not(i == 0 or i == altura-1):
        for j in range(largura):
            if not(j == 0 or j == largura-1): 
                print(' ', end = '')
            else:
                print('#', end = '')
    else:
        for j in range(largura):
            print('#', end = '')
        
    print()