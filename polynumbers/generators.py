'''
polynomial generators
'''
from geometor.utils import *
from geometor.model import *
from geometor.render import *

def Spread(n):
    n = sp.Integer(n)
    p = sp.Integer(0)
    for k in range(1, n+1):
        k = sp.Integer(k)
        # print('---')
        # print(k)
        next_term = sp.Poly(((-4)**(k-1))/(n+k) * sp.binomial(n+k,2*k) * x**k)
        # print(next_poly)
        p += next_term
        #  print(p)
    return 2*n*p

def Chebyshev(n):
    n = sp.Integer(n)

    p = sp.Poly((-((-1)**n+1)/2)**((n+4)/2))
    for i in range(1, n+1):
        i = sp.Integer(i)
        p += sp.Poly(n*(((-1)**(n+i)+1)/2 * (-1)**((n-i)/2)) * 2**(i-1) * \
                sp.factorial((n-2+i)//2)/(sp.factorial((n-i)//2) * sp.factorial(i)) * x**i)
    return p

