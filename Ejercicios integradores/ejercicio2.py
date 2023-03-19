import math



def mcm(a, b):
    return (a*b) // math.gcd (a, b)

print(mcm(20, 31))