# -*- coding: utf8 -*-
from phystricks import *
def ZPBMooYYMMgs():
    pspict,fig = SinglePicture("ZPBMooYYMMgs")
    pspict.dilatation(0.3)

    s=1
    ix=4
    A=Point(0,0)
    B=A+(3*ix,0)
    C=B+(s,ix)
    D=A+C-B

    parall=Polygon(A,B,C,D)
    #parall.put_mark(0.2,pspict=pspict)

    H=Point(C.x,B.y)
    mix=Segment(C,H).get_measure(measure_distance=-0.5,mark_distance=0.2,mark_angle=0,text="\( x\)",pspict=pspict)
    parall.edges[2].put_measure(measure_distance=0.5,mark_distance=0.2,mark_angle=90,text="\( 3x\)",pspict=pspict)

    no_symbol(parall.vertices)

    pspict.DrawGraphs(parall,mix)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
