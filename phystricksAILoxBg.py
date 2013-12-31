# -*- coding: utf8 -*-
from phystricks import *
def AILoxBg():
    pspict,fig = SinglePicture("AILoxBg")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(3,3)
    B=Point(0,3)
    C=Point(-3,0)
    D=Point(0,-3)
    E=Point(3,0)
    F=Point(3,-3)
    O=Point(0,0)

    A.put_mark(0.2,45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,135,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,-135,"\( C\)",automatic_place=(pspict,"corner"))
    D.put_mark(0.2,-45,"\( D\)",automatic_place=(pspict,"corner"))
    E.put_mark(0.2,-45,"\( E\)",automatic_place=(pspict,"corner"))
    F.put_mark(0.2,-45,"\( F\)",automatic_place=(pspict,"corner"))
    O.put_mark(0.2,45,"\( O\)",automatic_place=(pspict,"corner"))

    s1=Segment(C,B)
    s2=Segment(B,A)
    s3=Segment(A,F)
    s4=Segment(D,C)
    s5=Segment(F,D)
    s6=Segment(B,D)
    s7=Segment(C,E)

    pspict.DrawGraphs(A,B,C,D,E,F,O,s1,s2,s3,s4,s5,s6,s7)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

