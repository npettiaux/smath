# -*- coding: utf8 -*-
from phystricks import *
def KYVAooVmGYhS():
    pspict,fig = SinglePicture("KYVAooVmGYhS")
    pspict.dilatation_X(2)
    pspict.dilatation_Y(1.4)

    pr1=0.4
    pr2=0.7
    O=Point(0,0)
    P=Point(-0.5,3)
    Q=Point(4,3)
    A=Segment(O,P).get_point_proportion(pr1)
    B=Segment(O,P).get_point_proportion(pr2)
    C=Segment(O,Q).get_point_proportion(pr2)
    D=Segment(O,Q).get_point_proportion(pr1)
    
    p1=Segment(B,C).dilatation(1.3)
    p2=Segment(A,D).dilatation(2.1)
    d1=Segment(O,P)
    d2=Segment(O,Q)

    O.put_mark(0.1,angle=-45,text="\( K\)",pspict=pspict)

    a1=AngleAOB(C,B,P,r=0.3)
    a1.put_mark(text="\SI{100}{\degree}",pspict=pspict)
    a2=AngleAOB(p2.F,D,C)
    a2.put_mark(text="\SI{30}{\degree}",pspict=pspict)

    no_symbol(O)

    pspict.comment="Les angles sont marqués par de vrais arcs de cercles à l'écran"
    pspict.DrawGraphs(O,d1,d2,p1,p2,a1,a2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
