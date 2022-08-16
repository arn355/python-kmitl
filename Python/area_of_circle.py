import math

def area(r):
    return math.pi * (r**2)

r = float(input("r="))
print("Area=" + str(area(r)))
