from math import sqrt


def get_roots(parametr_a, parametr_b, parametr_c):
        discriminant = parametr_b**2 - 4*parametr_a*parametr_c
        if discriminant < 0:
          root1 = None
          root2 = None
          return root1, root2
        else:
          root1 = (-parametr_b-sqrt(discriminant))/(2*parametr_a)
          root2 = (-parametr_b+sqrt(discriminant))/(2*parametr_a)
        if discriminant == 0:
          return root1, None
        else:
          return root1, root2


if __name__ == '__main__':
    get_roots(a,b,c)