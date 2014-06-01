# -*- coding: utf8 -*-
from phystricks import *
def VFAooZmuvtW():
    pspict,fig = SinglePicture("VFAooZmuvtW")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    mx=-3
    Mx=7

    x=var('x')
    F=[]
    F.append(phyFunction((x+2)/(2*x-6)).graph(mx,Mx))

    for f in F:
        f.cut_y(-4,4)

    import random
    random.shuffle(F)

    pspict.DrawGraphs(F)
    #pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
