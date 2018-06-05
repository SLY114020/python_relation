# -*- coding: utf-8 -*-

import logging
from functools import reduce

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
logging.info('n=%d' % n)
print(10 / n)


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
        