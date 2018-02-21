# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:20:44 2016

@author: Nedeljko Stefanović
"""
from resource import *

def g(n):
    if n<3:
        return 0
    x = n
    n2 = n*n
    while True:
        xn = (x*x+n2-1)//(2*(x+n))+1
        if xn==x:
            return x-1
        x = xn

def f(n):
    s = n*(n+1)//2
    positive = True
    while n>=3:
        k = g(n)
        if positive:
            s += k*(n-k-1)
        else:
            s -= k*(n-k-1)
        positive = not positive
        n = k
    return s

n = 12763276378643876438763287634876438764387648764876487648764876487643876487643876

print(f(n))

# The next line must be commented in case of Windows system.
print(getrusage(RUSAGE_SELF))

