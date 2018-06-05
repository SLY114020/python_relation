# -*- coding: utf-8 -*-

import logging
from functools import reduce
import os
import pickle
import json

logging.basicConfig(level=logging.INFO)


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')


def str2num(s):
    try:
        return int(s)
    except Exception as e:
        return float(s)
    return 0


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def calc2():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


calc2()


def fooAssert(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


# fooAssert('0')

s = '0'
n = int(s)

# logging.info('n=%d' % n)
# print(10 / n)


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Dict object has no attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'

with open('./pythonStudy/test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

with open('./pythonStudy/byteFile.txt', 'wb') as f:
    f.write(b'\x41\x42')
    f.write('\n'.encode('utf-8'))
    f.write(b'\x43\x44')
with open('./pythonStudy/byteFile.txt', 'rb') as f:
    print(f.read().decode('utf-8'))

print(os.name)
# window 下不提供这个函数
# print(os.uname())

# print(os.environ.get('PATH'))
'''
print(os.path.abspath('.'))
newFile = os.path.join(os.path.abspath('.'), 'testdir')
os.mkdir(newFile)
os.rmdir(newFile)
'''

d = dict(name='Bob', age=20, score=88)
str = pickle.dumps(d)
d1 = pickle.loads(str)
print(d1)
str = json.dumps(d1)
print(str)
d1 = json.loads(str)
print(d1)

obj = dict(name='小明', age=20)
print(obj)
s = json.dumps(obj, ensure_ascii=True)
print(s)
d1 = json.loads(s)
print(d1)


