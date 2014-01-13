# -*- coding: utf8 -*-
from phystricks import *

from phystricksFFyFBoe import f

def EJbcoxO():
    pspict,fig = SinglePicture("EJbcoxO")
    pspict.dilatation_X(2)
    pspict.dilatation_Y(1.3)

    x=var('x')
    
    droite1=Segment( Point(-1,1),Point(2,1) )
    droite1.parameters.color="red"

    #pts=Intersection(droite1,f)
    #A=pts[0]
    #B=pts[1]
    A=Point(0.5,1)
    B=Point(1.26,1)
    A.put_mark(0.2,90,"\( A\)",automatic_place=(pspict,"S"))
    B.put_mark(0.2,90,"\( B\)",automatic_place=(pspict,"S"))

    Z1=Point(-1.91,0)
    Z2=Point(0,0)
    Z3=Point(1.91,0)
    Z1.put_mark(0.2,90,"\( Z_1\)",automatic_place=(pspict,"S"))
    Z2.put_mark(0.2,135,"\( Z_2\)",automatic_place=pspict)
    Z3.put_mark(0.2,90,"\( Z_3 \)",automatic_place=(pspict,"S"))

    M=Point(0.86,f(0.86))
    M.put_mark(0.2,90,"\( M\)",automatic_place=(pspict,"S"))

    pspict.DrawGraphs(f,droite1,A,B,Z1,Z2,Z3,M)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()