""" This script calculates quadratic functions"""

# todo: add click options

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


def main():
    print("Result =", solve_quad(a1, b1, c1))
    print("Result =", solve_quad(a2, b2, c2))
    print("Result =", solve_quad(a3, b3, c3))
    print("Result =", solve_quad(a4, b4, c4))


def cal_d(a: float, b: float, c: float) -> float:
    """
    This function calculates discriminant:
    :parameter a(float) - first number (a * x^2)
    :parameter b(float) - second number (b * x)
    :parameter c(float) - third number (c)

    :return disc(float) - resulting discriminant
    """
    disc = b**2 - 4 * a * c
    return disc


def solve_quad(a: float, b: float, c: float) -> list[float, float] or float or None:
    """
    This script return x value or values that will be appropriate for this quadratic function
    :parameter a(float) - first number (a * x^2)
    :parameter b(float) - second number (b * x)
    :parameter c(float) - third number (c)
    :return: x - depending on the inputs is either a list of [x1, x2], just x or None if no solutions
    """
    discriminant = cal_d(a, b, c)
    print("Discriminant =", discriminant)
    if discriminant > 0:
        x1 = (-b + discriminant ** (1 / 2)) / (2 * a)
        x2 = (-b - discriminant ** (1 / 2)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = (-b) / (2 * a)
        return x
    else:
        x = None
        return x


if __name__ == "__main__":
    main()
