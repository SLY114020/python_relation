
# -*- coding: utf-8 -*-
from functools import reduce


def add(x, y):
	return x + y
	
print(reduce(add, [1,2,3,4,5]))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def normalize(name):
	return name[:1].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
print(list(map(normalize, L1)))

def prod(L):
	return reduce(lambda x,y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def str2float(s):
	DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': True}
	def char2int(s):
		return DIGITS[s]
	def fn(x, y):
		if type(y).__name__ == 'bool':
			return x, 10
		if type(x).__name__ == 'tuple':
			num = x[0] + y * 1.0 / x[1]
			return num, x[1] * 10
		return x * 10 + y
	num = reduce(fn, map(char2int, s))
	return num[0]
print('str2float(\'123.456\') =', str2float('123.456'))

def is_odd(n):
	return n % 2 == 1
	
print(list(filter(is_odd, [1,2,3,4,5,6])))
print(list(filter(lambda x: x%2 == 1, range(1, 20))))


def is_palindrome(n):
	resver_n = 0
	tmp = n
	while tmp > 0:
		num = tmp % 10
		tmp = tmp / 10
		resver_n = resver_n * 10 + num
	return resver_n == n

if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功1!')
else:
    print('测试失败2!')

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0].lower()
	
def by_score(t):
	return t[1]
	
L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score)
print(L2)

def createCounter():
	i = [0]
	def counter():
		i[0] = i[0] + 1
		return i[0]
	return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过1!')
else:
    print('测试失败2!')











