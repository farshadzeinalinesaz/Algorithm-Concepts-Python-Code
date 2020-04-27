#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:22:52 2020

@author: farshad
"""

def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)


result=factorial(10)
print(result)