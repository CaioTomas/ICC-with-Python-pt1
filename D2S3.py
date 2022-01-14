a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4*a*c

if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    raiz = (-b)/(2*a)
    print('a raiz dupla desta equação é', raiz)
else:
    raiz1 = (-b + (delta)**(0.5))/(2*a)
    raiz2 = (-b - (delta)**(0.5))/(2*a)
    if raiz1 > raiz2:
        print('as raízes da equação são', raiz2, 'e', raiz1)
    else:
        print('as raízes da equação são', raiz1, 'e', raiz2)