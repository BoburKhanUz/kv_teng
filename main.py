import math

a = float(input("a sonini kiriting: "))
b = float(input("b sonini kiriting: "))
c = float(input("c sonini kiriting: "))

d = math.sqrt(b * b - 4 * a * c)
if a!=0:
    if d >= 0:
            x1=(b+d) / (2 * a)
            x2=(b-d) / (2 * a)
            print ("Javob x1=" , x1)
            print ("Javob x2=" , x2)
    if d == 0:
            x1=b/ (2 * a)
            print("Javob x1=" , x1)
    else:
         print ("Javob mavjud emas!")
else:
    print ("A nolga teng emas!")