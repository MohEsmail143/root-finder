from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def bisection(xl, xu, f, es, imax):
    res_ar = []
    xr = 0
    ea = 1
    i = 0
    if f(xl) * f(xu) > 0:
        # print("Incorrect bracket")
        return
    else:
        # print(f"i\txl\txu\txr\tf(xl)\t\tf(xr)\tea")
        for i in range(imax):
            temp_ar = []
            if i > 0:
                xr_prev = xr
            xr = (xl + xu) / 2
            temp_ar.append(i + 1)
            temp_ar.append(round(xl, 5))
            temp_ar.append(round(f(xl), 5))
            temp_ar.append(round(xu, 5))
            temp_ar.append(round(f(xu), 5))
            temp_ar.append(round(xr, 5))
            temp_ar.append(round(f(xr), 5))

            if f(xl) * f(xr) == 0:
                break
            elif f(xl) * f(xr) < 0:
                xu = xr
            else:
                xl = xr
            if i > 0:
                ea = abs((xr - xr_prev) / xr)
                temp_ar.append(round(ea, 5))
                # print(f"{i}\t{xl}\t{xu}\t{xr}\t{f(xl)}\t{f(xr)}\t{ea}")
                if ea < es:
                    break
            else:
                temp_ar.append("")
            res_ar.append(temp_ar)
        temp_ar = []
        temp_ar.append(i + 1)
        temp_ar.append(round(xl, 5))
        temp_ar.append(round(f(xl), 5))
        temp_ar.append(round(xu, 5))
        temp_ar.append(round(f(xu), 5))
        temp_ar.append(round(xr, 5))
        temp_ar.append(round(f(xr), 5))
        temp_ar.append(round(ea, 5))
        res_ar.append(temp_ar)

    return res_ar


def false_position(xl, xu, f, es, imax):
    xr = 0
    res_ar = []
    if f(xl) * f(xu) > 0:
        # print("Incorrect bracket")
        return
    else:
        # print(f"i\txl\txu\txr\tf(xl)\t\tf(xr)\tea")
        for i in range(imax):
            temp_ar = []
            if i > 0:
                xr_prev = xr
            xr = (xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl))
            temp_ar.append(i + 1)
            temp_ar.append(round(xl, 5))
            temp_ar.append(round(f(xl), 5))
            temp_ar.append(round(xu, 5))
            temp_ar.append(round(f(xu), 5))
            temp_ar.append(round(xr, 5))
            temp_ar.append(round(f(xr), 5))

            if f(xr) == 0:
                break
            elif f(xr) < 0:
                xl = xr
            else:
                xu = xr
            if i > 0:
                ea = abs((xr - xr_prev) / xr)
                temp_ar.append(round(ea, 5))
                # print(f"{i}\t{xl}\t{xu}\t{xr}\t{f(xl)}\t{f(xr)}\t{ea}")
                if ea < es:
                    break
            else:
                temp_ar.append("")
            res_ar.append(temp_ar)
        temp_ar = []
        temp_ar.append(i + 1)
        temp_ar.append(round(xl, 5))
        temp_ar.append(round(f(xl), 5))
        temp_ar.append(round(xu, 5))
        temp_ar.append(round(f(xu), 5))
        temp_ar.append(round(xr, 5))
        temp_ar.append(round(f(xr), 5))
        temp_ar.append(round(ea, 5))
        res_ar.append(temp_ar)

    return res_ar


def fixed_point(x, g, es, imax):
    res_ar = []
    xr = x
    for i in range(imax):
        temp_ar = []
        xr_old = xr
        xr = g(xr_old)
        temp_ar.append(i + 1)
        temp_ar.append(round(xr_old, 5))
        temp_ar.append(round(xr, 5))
        if (xr != 0):
            ea = abs((xr - xr_old) / xr)
            temp_ar.append(round(ea, 5))
            if ea < es:
                break
        res_ar.append(temp_ar)
    temp_ar = []
    temp_ar.append(i + 1)
    temp_ar.append(round(xr_old, 5))
    temp_ar.append(round(xr, 5))
    temp_ar.append(round(ea, 5))
    res_ar.append(temp_ar)

    return res_ar


def newton_raphson(x_0, eq, es, imax):
    res_ar = []
    x = Symbol('x')
    f = lambda x: eval(eq)
    y = parse_expr(eq)
    yprime = y.diff(x)
    xr = x_0
    for i in range(imax):
        temp_ar = []
        ea = 1
        xr_old = xr
        temp_ar.append(i + 1)
        temp_ar.append(round(xr_old, 5))
        # temp_ar.append(round(f(xr_old), 3))
        if float(yprime.subs(x, xr)) != 0:
            xr = xr - (f(xr) / float(yprime.subs(x, xr)))
            # temp_ar.append(round(float(yprime.subs(x, xr_old)), 3))
            temp_ar.append(round(xr, 5))
            if xr != 0:
                ea = abs((xr - xr_old) / xr)
                temp_ar.append(round(ea, 5))
                if ea < es:
                    break
        res_ar.append(temp_ar)
    temp_ar = []
    temp_ar.append(i + 1)
    temp_ar.append(round(xr_old, 5))
    temp_ar.append(round(xr, 5))
    temp_ar.append(round(ea, 5))
    res_ar.append(temp_ar)

    return res_ar


def secant(x_iminus1, xi, f, es, imax):
    res_ar = []
    xr = xi
    for i in range(imax):
        temp_ar = []
        temp_ar.append(i + 1)
        temp_ar.append(round(x_iminus1, 5))
        if i > 0:
            x_iminus1 = xi

        xi = xr
        temp_ar.append(round(xi, 5))
        xr = xi - (f(xi) * (x_iminus1 - xi)) / (f(x_iminus1) - f(xi))
        temp_ar.append(round(f(x_iminus1), 5))
        temp_ar.append(round(f(xi), 5))
        if (xr != 0):
            ea = abs((xr - xi) / xr)
            temp_ar.append(round(ea, 5))
            if ea < es:
                break
        res_ar.append(temp_ar)
    temp_ar = []
    temp_ar.append(i + 1)
    temp_ar.append(round(x_iminus1, 5))
    temp_ar.append(round(xi, 5))
    temp_ar.append(round(f(x_iminus1), 5))
    temp_ar.append(round(f(xi), 5))
    temp_ar.append(round(ea, 5))
    res_ar.append(temp_ar)
    return res_ar
