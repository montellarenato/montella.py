ax = int(input("quanto vale ax"))

bx = int(input("quanto vale bx"))

c = int(input("quanto vale c"))

import math

delta = pow(bx,2)-4*ax*c

if delta < 0:

    print("non ci sono soluzioni")

elif delta > 0:
    print(str("ci sono 2 soluzioni reali:"))
    print(str("x1="))
    print(int((-1*bx)-(math.sqrt(delta))) / (2*ax))
    print(str("x2="))
    print(int((-1*bx)+(math.sqrt(delta))) / (2*ax))

if c == 0:
    print(str("ci sono 2 soluzioni:"))
    print(str("x1="))
    print(str("sempre uguale a 0"))
    print(str("x2="))
    print(int((-1*bx)) / (ax))

elif bx == 0:
    print(str("ci sono 2 soluzioni reali:"))
    print(str("x1="))
    print(int(-1*(math.sqrt(-1*c/ax))))
    print(str("x2="))
    print(int(math.sqrt(-1*c/ax)))


