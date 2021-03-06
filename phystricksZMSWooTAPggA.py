# -*- coding: utf8 -*-
from phystricks import *
def ZMSWooTAPggA():
    pspict,fig = SinglePicture("ZMSWooTAPggA")
    pspict.dilatation_X(1.7)
    pspict.dilatation_Y(1)

    mx=-5
    Mx=4.7

    O=Point(0,0)
    #A=Point(-3,0)
    #B=Point(4,0)

    O.put_mark(0.2,text="\( O\)",pspict=pspict,position="N")
    #B.put_mark(0.2,-90,"\( B\)",pspict=pspict,position="N")

    for i in range(mx,0):
        A=Point(i,0)
        A.parameters.symbol=""
        if i%2==0 :
            A.put_mark(0.2,text="\(  {}\)".format(i),pspict=pspict,position="N")
        else:
            A.put_mark(0.2,text="\( {}\)".format(i),pspict=pspict,position="N")
        pspict.DrawGraphs(A)
    for i in range(0,floor(Mx)+1):
        A=Point(i,0)
        A.parameters.symbol=""
        A.put_mark(0.2,text="\( {}\)".format(i),pspict=pspict,position="N")
        pspict.DrawGraphs(A)

    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    axe.no_numbering()

    pspict.DrawGraphs(axe)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
