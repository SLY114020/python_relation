# -*- coding: utf-8 -*-

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x
		
print(my_abs(-99))

def fib(max):
	n, a, b = 0,0,1
	while n < max:
		print(b)
		a, b = b, a+b
		n = n + 1
	return n
#print(fib(2))

def triangles():
	n = 0
	l = [1]
	while True:
		yield l
		ll = len(l) - 1
		l.append(1)
		while ll >= 1:
			l[ll] = l[ll - 1] + l[ll]
			ll = ll - 1

n = 0
results = []
for t in triangles():
    results.append(t[:])
    n = n + 1
    if n == 10:
        break
			
for v in results:
	print(v)



