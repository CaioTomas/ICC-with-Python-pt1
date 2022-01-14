def maximo(x,y,z):
    max = None

    if x>=y:
        if x>=z:
            max = x
        else:
            max = z
    else:
        if y>=z:
            max = y
        else:
            max = z
    return max

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(maximo(num1,num2,num3))