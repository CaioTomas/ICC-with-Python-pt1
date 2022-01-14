n = int(input('Digite um número inteiro: '))

num = str(n)

cont = 0
sim = 0
i = 0

while cont in range(len(num)-1):
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            sim = 1
    cont += 1
if sim == 0:
    print('não')
else:
    print('sim')
        