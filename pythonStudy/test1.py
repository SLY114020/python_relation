
# -*- coding: utf-8 -*-
from test import my_abs
import math

my_abs(-99)

def quadratic(a, b, c):
	f1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
	f2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
	return f1, f2
	
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
if quadratic(2, 3, 1) != (-0.5, -1.0):
	print("test fail")
elif quadratic(1, 3, -4) != (1.0, -4.0):
	print('test fail')
else: 
	print('sucess')
	
	
def add_end(L=[]):
	L.append('End')
	return L
print(add_end())
print(add_end())

def calc(*number):
	sum = 0
	for n in number:
		sum = sum + n*n
	return sum

print(calc(1,2,3))
print(calc(1,3,6,7))
ll = [1,2,3]
calc(*ll)

def person(name, age, **kv):
	print(name, age, kv)
person('sly', 10, city='beijing', gender='M')
extra = {'city':'begin', 'gender':'M'}
person('huang', 12, **extra)


def product(*number):
	if not number:
		raise TypeError(' «ø’÷µ')
	result = 1
	for n in number:
		result = result*n
	return result

if product(5) != 5:
    print('≤‚ ‘ ß∞‹!')
elif product(5, 6) != 30:
    print('≤‚ ‘ ß∞‹!')
elif product(5, 6, 7) != 210:
    print('≤‚ ‘ ß∞‹!')
elif product(5, 6, 7, 9) != 1890:
    print('≤‚ ‘ ß∞‹!')
else:
    try:
        product()
        print('≤‚ ‘ ß∞‹!')
    except TypeError:
        print('≤‚ ‘≥…π¶!')


		
def trim(s):
	sSize = len(s)
	begin = 0
	end = sSize - 1
	while begin <= end:
		if s[begin] == ' ':
			begin = begin + 1
		else:
			break
	while begin <= end:
		if s[end] == ' ':
			end = end - 1
		else: 
			break
	return s[begin:end+1]
if trim('hello  ') != 'hello':
    print('≤‚ ‘ ß∞‹1!')
elif trim('  hello') != 'hello':
    print('≤‚ ‘ ß∞‹2!')
elif trim('  hello  ') != 'hello':
    print('≤‚ ‘ ß∞‹3!')
elif trim('  hello  world  ') != 'hello  world':
    print('≤‚ ‘ ß∞‹4!')
elif trim('') != '':
    print('≤‚ ‘ ß∞‹5!')
elif trim('    ') != '':
    print('≤‚ ‘ ß∞‹6!')
else:
    print('≤‚ ‘≥…π¶!')


def findMinAndMax(L):
	if not L:
		return None,None
	max = L[0]
	min = L[0]
	for v in L:
		if v > max:
			max = v
		if v < min:
			min = v;
	return min, max

if findMinAndMax([]) != (None, None):
    print('≤‚ ‘ ß∞‹!')
elif findMinAndMax([7]) != (7, 7):
    print('≤‚ ‘ ß∞‹!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('≤‚ ‘ ß∞‹!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('≤‚ ‘ ß∞‹!')
else:
    print('≤‚ ‘≥…π¶!')	
	
	
	
L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])
	
	
	
	
	