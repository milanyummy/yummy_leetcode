# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:29:34 2020

@author: YummY
"""
def minimumLengthEncoding(words):
    return (lambda r:sum([len(r[i])+1 for i in range(len(r)) if i==len(r)-1 or not r[i+1].startswith(r[i])]) )(sorted([w[::-1] for w in words]))
words = ["time", "me", "bell"]

print(minimumLengthEncoding(words))