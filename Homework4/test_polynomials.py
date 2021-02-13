from polynomials import *
from Homework4.polynomials import evaluate, bisection

# When the input is "E1.0 -945 1689 -950 230 -25 1"

x = 1.0
poly = [-945, 1689, -950, 230, -25, 1]

print(evaluate(x, poly))

# When the input is "S0 2 -945 1689 -950 230 -25 1 1e-15"

a = 0
b = 2
poly = [-945, 1689, -950, 230, -25, 1]
tol = 1e-15

print(bisection(a, b, poly, tol))
