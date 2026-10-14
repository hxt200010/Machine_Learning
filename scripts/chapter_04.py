# Central difference approximates the derivative of f(x) = x^3.
def f(x): return x**3
x, h = 2., 1e-4
numerical = (f(x+h)-f(x-h))/(2*h)
exact = 3*x*x
print('Numerical derivative:', round(numerical, 6))
print('Exact derivative:', exact)
print('Absolute error:', round(abs(numerical-exact), 10))
