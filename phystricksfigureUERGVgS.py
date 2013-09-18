# -*- coding: utf8 -*-
from phystricks import *
def figureUERGVgS():
    pspict,fig = SinglePicture("figureUERGVgS")
    pspict.dilatation(0.7)

    x=var('x')
    f=phyFunction(3*x/4+3).graph(-3,4)

    l=2  # C'est la distance à laquelle on met le second point
    O=Point(0,0)
    O.put_mark(0.2,225,"\( O\)",automatic_place=pspict)
    B=Point(0,f(0))
    #B.put_mark(0.2,135,"\( p\)",automatic_place=pspict)
    A=Point(2,f(l))
    X=Point(l,f(0))
    I=Point(l,0)
    I.put_mark(0.2,-90,"\( I\)",automatic_place=(pspict,"N"))
    seg=Segment(B,X)
    seg.parameters.style="dashed"

    measure=MeasureLength(Segment(X,A),0.1)
    measure.put_mark(0.2,0,"\( m\)",automatic_place=pspict)

    measureB=MeasureLength(Segment(O,B),0.2)
    measureB.put_mark(0.2,0,"\( p\)",automatic_place=pspict)

    #I=Point(1,0)
    #J=Point(0,1)

    #I.put_mark(0.2,-90,"\( I\)",automatic_place=pspict)
    #J.put_mark(0.2,180,"\( J\)",automatic_place=pspict)

    pspict.DrawGraphs(f,O,B,seg,measure,I,measureB)

    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
