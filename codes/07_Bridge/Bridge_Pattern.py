#!/usr/bin/python
#coding:utf8
'''
Bridge
'''


# ConcreteImplementor 1/2
class DrawAPI1(object):
    def draw_circle(self,x,y,radius):
        print('API1.circle a {}:{} radius {}'.format(x,y,radius))

# ConcreteImplementor 2/2
class DrawAPI2(object):
    def draw_circle(self,x,y,radius):
        print('API2.circle a {}:{} radius {}'.format(x,y,radius))


# Refined Abstraction
class CircleShape(object):
    def __init__(self,x,y,radius,drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x,self._y,self._radius)

    def scale(self,pct):
        self._radius *=pct

def main():
    shapes = (
        CircleShape(1,2,3,DrawAPI1()),
        CircleShape(5, 7, 11, DrawAPI2())
    )

    for shape in shapes:
        shape.scale(2)
        shape.draw()


if __name__ == '__main__':
    main()