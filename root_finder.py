from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def bisection(xl, xu, f, es, imax):
    global xr
    if f(xl) * f(xu) > 0:
        print("Incorrect bracket")
        return
    else:
        print(f"i\txl\txu\txr\tf(xl)\t\tf(xr)\tea")
        for i in range(imax):
            if i > 0:
                xr_prev = xr
            xr = (xl + xu) / 2

            if f(xl) * f(xr) == 0:
                break
            elif f(xl) * f(xr) < 0:
                xu = xr
            else:
                xl = xr
            if i > 0:
                ea = abs((xr - xr_prev) / xr)
                print(f"{i + 1}\t{xl}\t{xu}\t{xr}\t{f(xl)}\t{f(xr)}\t{ea}")
                if ea < es:
                    break
    return xr


def false_position(xl, xu, f, es, imax):
    global xr
    if f(xl) * f(xu) > 0:
        print("Incorrect bracket")
        return
    else:
        print(f"i\txl\txu\txr\tf(xl)\t\tf(xr)\tea")
        for i in range(imax):
            if i > 0:
                xr_prev = xr
            xr = (xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl))

            if f(xr) == 0:
                break
            elif f(xr) < 0:
                xl = xr
            else:
                xu = xr
            if i > 0:
                ea = abs((xr - xr_prev) / xr)
                print(f"{i + 1}\t{xl}\t{xu}\t{xr}\t{f(xl)}\t{f(xr)}\t{ea}")
                if ea < es:
                    break
    return xr


def fixed_point(x, g, es, imax):
    xr = x
    for i in range(imax):
        xr_old = xr
        xr = g(xr_old)
        if (xr != 0):
            ea = abs((xr - xr_old) / xr)
            if ea < es:
                break
    return xr


def newton_raphson(x_0, eq, es, imax):
    x = Symbol('x')
    f = lambda x: eval(eq)
    y = parse_expr(eq)
    yprime = y.diff(x)
    xr = x_0
    for i in range(imax):
        xr_old = xr
        if float(yprime.subs(x, xr)) != 0:
            xr = xr - (f(xr) / float(yprime.subs(x, xr)))
            if (xr != 0):
                ea = abs((xr - xr_old) / xr)
                if ea < es:
                    break
    return xr


def secant(x_iminus1, xi, f, es, imax):
    xr = xi
    for i in range(imax):
        if i > 0:
            x_iminus1 = xi
        xi = xr
        xr = xi - (f(xi) * (x_iminus1 - xi)) / (f(x_iminus1) - f(xi))
        if (xr != 0):
            ea = abs((xr - xi) / xr)
            if ea < es:
                break
    return xr


if __name__ == '__main__':
    print("Welcome to the Numerical Analysis Equation Solver!\n")
    eq = input("f(x) = ")
    f = lambda x: eval(eq)
    # print(f(2.5))
    es = float(input("es = "))
    imax = int(input("imax = "))
    method = input(
        "Please select your preferred method:\n1- Bisection\n2- False-position\n3- Fixed point\n4- Newton-Raphson\n5- Secant\n\n>> ")
    if method == '1':
        xl = float(input("xl = "))
        xu = float(input("xu = "))
        print(bisection(xl, xu, f, es, imax))
    elif method == '2':
        xl = float(input("xl = "))
        xu = float(input("xu = "))
        print(false_position(xl, xu, f, es, imax))
    elif method == '3':
        x = float(input("x = "))
        print(fixed_point(x, f, es, imax))
    elif method == '4':
        x = float(input("x = "))
        print(newton_raphson(x, eq, es, imax))
    elif method == '5':
        x_iminus1 = float(input("x_iminus1 = "))
        xi = float(input("xi = "))
        print(secant(x_iminus1, xi, f, es, imax))
