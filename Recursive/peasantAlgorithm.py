#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:39:06 2020

@author: farshad
@email : fzcomputerscience@gmail.com
"""

def peasantMultiplication(x,y):
    if(x==0):
        return 0
    x1 = x/2
    y1 = y + y
    result = peasantMultiplication(x1,y1)
    if(x % 2 == 0):
        return result
    else:
        return result + y
    

result = peasantMultiplication(2,3)
print(result)



