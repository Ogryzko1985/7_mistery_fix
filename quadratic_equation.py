from math import sqrt
a = int(input("Print a:"))
print(a)
b = int(input("Print b:"))
print(b)
c = int(input("Print c:"))
print(c)


def get_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        root1 = None
        root2 = None
    return root1, root2
    else:
        root1 = (-b-sqrt(discriminant))/(2*a)
        root2 = (-b+sqrt(discriminant))/(2*a)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2
f = get_roots(a, b, c)
print(f)
