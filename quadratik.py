""" Эта программа решает квадратное уравнение методом дискрименанта """

a1 = 1
b1 = -5
c1 = 6
a2 = 2
b2 = 3
c2 = -2
a3 = 1
b3 = 4
c3 = 8
a4 = 2
b4 = 4
c4 = 2


def cal_d(a, b, c):
    """Эта функция вычисляет дискриминант"""
    disc = b**2 - 4*a*c
    return disc


def solve_quad(a, b, c):
    """Эта функция решает квадратное уравнение"""
    D = cal_d(a, b, c)
    print('Дискриминат =', D)
    if D > 0:
        x1 = (-b + D**(1/2)) / (2*a)
        x2 = (-b - D**(1/2)) / (2*a)
        return x1, x2
    elif D == 0:
        x = (-b) / (2*a)
        return x
    else:
        x = None
        return x


print(solve_quad(a1, b1, c1))
print(solve_quad(a2, b2, c2))
print(solve_quad(a3, b3, c3))
print(solve_quad(a4, b4, c4))





