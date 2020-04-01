# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:56:05 2020

@author: YummY
"""

deck = [1,1,1,1,1,1,1,1,1]
times = []
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
deckSet = set(deck)
for item in deckSet:
    times.append(deck.count(item))
length = len(times)
if length == 1:
    if times >= 2:
        return True
    else:
        return False
X =  gcd(times[0], times[1])
if X < 2:
    print(X)
for i in range(2, length):
    temp = gcd(X, times[i])
    print (temp)
    if temp < 2:
        print(temp)
    if temp < X:
        X = temp
        print(X)
