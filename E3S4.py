n = int(input('Digite um número inteiro: '))

num = str(n)

i = 0
soma = 0

while i < len(num):
    soma += int(num[i])
    i += 1
print(soma)