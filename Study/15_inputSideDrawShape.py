# -*- coding: cp936 -*-
import turtle
def DrawShape(sides,length):
    angle=360/sides
    for again in range(sides):
        turtle.forward(length)
        turtle.right(angle)

side=int(raw_input("��������Ҫ����ͼ�εı�����"))
length=int(raw_input('��������Ҫ����ͼ�εı߳���'))
DrawShape(side,length)
turtle.done()
