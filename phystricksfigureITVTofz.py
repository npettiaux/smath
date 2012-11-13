# -*- coding: utf8 -*-
from phystricks import *
def figureITVTofz():
    pspict,fig = SinglePicture("figureITVTofz")
    pspict.dilatation(1.2)

    A=Point(0,0)
    B=Point(4,0)
    C=Point(3,3)

    A.put_mark(0.2,180,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,0,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,90,"\( C\)",automatic_place=pspict)

    AB=Segment(A,B)
    BC=Segment(B,C)
    CA=Segment(C,A)

    KA=A.projection(BC)
    KA.put_mark(0.2,0,"\( I\)",automatic_place=pspict)
    hA=Segment(A,KA)
    KB=B.projection(CA)
    KB.put_mark(0.2,135,"\( J\)",automatic_place=pspict)
    hB=Segment(B,KB)
    KC=C.projection(AB)
    KC.put_mark(0.2,-90,"\( K\)",automatic_place=pspict)
    hC=Segment(C,KC)

    hA.parameters.color="red"
    hB.parameters.color="red"
    hC.parameters.color="red"

    G=Intersection(hA,hB)[0]
    G.put_mark(0.4,-90,"\( H\)",automatic_place=pspict)


    pspict.DrawGraphs(hA,hB,hC,AB,BC,CA,KA,KB,KC,G,A,B,C)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
