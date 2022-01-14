largura = int(input('digite a largura: ').split()[0])
altura = int(input('digite a altura: ').split()[0])

for i in range(altura):
    for j in range(largura):
        print('#', end = '')
    print()