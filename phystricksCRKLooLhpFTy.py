# -*- coding: utf8 -*-
from phystricks import *
def CRKLooLhpFTy():
    pspict,fig = SinglePicture("CRKLooLhpFTy")
    pspict.dilatation(1)

    r=3
    A=Point(0,0)
    B=Circle(A,r).get_point(30)
    C=Circle(A,r).get_point(-30)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspict=pspict)

    angA=AngleAOB(C,A,B)
    angB=AngleAOB(A,B,C)
    angC=AngleAOB(B,C,A)

    for P in trig.vertices:
        P.parameters.symbol=''

    angA.put_mark(0.2,None,"\(60 \)",automatic_place=(pspict,"center"))
    angB.put_mark(0.2,None,"\( 60 \)",automatic_place=(pspict,"center"))
    angC.put_mark(0.2,None,"\( 60 \)",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(trig,angA,angB,angC)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
