def maximo(x,y):
    max = None

    if x >= y:
        max = x
    else:
        max = y
    return max

x = float(input())
y = float(input())

print(maximo(x,y))