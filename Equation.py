import numpy as np

"""
Function in charge of telling the script what your wanted graph equation is.
In order for the script to work in the most optimal way, you must use 
numpy functions when possible.
The numpy math function are described in the following link:
https://numpy.org/doc/stable/reference/routines.math.html

I have given ax example here.

Requirements:
The first argument must be x - the dependent factor in the equation.
Following x are the constants which we would like to find.
They must be given as arguments in the same order as used in the equation!  
"""
def equation(x, a, b, c):
    return a * x + np.exp(b*x) + c
