num = int(input('Digite um número: '))

lst = []

while num != 0:
    lst.append(num)
    num = int(input('Digite um número: '))
else:
    print()
    
k = 1
while k <= len(lst):
    print(lst[len(lst) - k])
    k += 1
