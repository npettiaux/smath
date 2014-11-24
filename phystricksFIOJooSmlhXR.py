# -*- coding: utf8 -*-
from phystricks import *
def FIOJooSmlhXR():
    pspicts,figs = IndependentPictures("FIOJooSmlhXR",2)
    for psp in pspicts:
        psp.dilatation(0.56)

    L=10
    l=4
    h=3
    A=Point(0,0)
    B=A+(l,0)
    C=A+(L,0)
    D=C+(0,h)
    E=B+(0,h)
    F=A+(0,h)

    jardin=Polygon(A,B,E,F)
    piscine=Polygon(B,C,D,E)
    piscine.parameters.hatched()
    piscine.parameters.hatch.color="lightgray"

    mesL=Segment(F,D).get_measure(-0.2,0.1,90,"\( 10\)",automatic_place=(pspicts,"S"))
    mesl=Segment(A,B).get_measure(0.2,0.1,-90,"\( x\)",automatic_place=(pspicts,"N"))
    mesH=Segment(A,F).get_measure(-0.2,0.1,180,"\( 3\)",automatic_place=(pspicts,"E"))
    mesP=Segment(B,C).get_measure(0.2,0.1,-90,"\( 10-x\)",automatic_place=(pspicts,"N"))

    pspicts[0].DrawGraphs(piscine,jardin,mesL,mesl,mesH)
    pspicts[1].DrawGraphs(piscine,jardin,mesL,mesl,mesH,mesP)

    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()