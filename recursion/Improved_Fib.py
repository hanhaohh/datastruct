#!/usr/bin/env python
#encoding= "utf-8"

def imp_fib(n):
	if n<=1:
		a,b = (1,0)
	else:
		#this method make the time complexity O(n) rather than O(2^n),becaushe it can avoid for computing redudance.
		(a, b) = imp_fib(n−1)
	return (a+b,b)
