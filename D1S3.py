x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

dist = ( (x1 - x2)**2 + (y1 - y2)**2 )**(0.5) 

if dist < 10:
    print('perto')
else:
    print('longe')