#!/usr/bin/env python
# coding: utf-8

def factorielle(n) :
    if n == 0:
        return 1
    else :
        return n * factorielle(n-1)

factorielle(5)