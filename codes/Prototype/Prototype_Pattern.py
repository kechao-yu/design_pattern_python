#!/usr/bin/python
# coding:utf-8


'''
Prototype Pattern
'''

import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        '''Register an object'''
        self._objects[name] = obj

    def unregister_object(self, name):
        '''Unregiester an object'''
        del self._objects[name]

    def clone(self, name, **attr):
        '''Clone a registered object and update inner attributes dictionary'''
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


def main():
    class A:
        def __str__(self):
            return "I am A"

    a = A()

    prototype = Prototype()
    prototype.register_object('a', a)
    b = prototype.clone('a', a=1, b=2, c=3)
    print(a)
    print(b.a, b.b, b.c)
    # c = prototype.clone('a', x=100, y=1000, z=10000)
    # print(c)
    # print(c.x, c.y, c.z)


if __name__ == '__main__':
    main()
