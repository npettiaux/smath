#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun
import enseignement

tous=enseignement.tous
groupe_4A=enseignement.groupe_4A
groupe_5A=enseignement.groupe_5A
groupe_5B=enseignement.groupe_5B
groupe_5AB=groupe_5A.extend(groupe_5B,"groupe_5AB")

DS1_5B=commun.TheDS("DS1_5B",groupe_5B,1)
DS2_5AB=commun.TheDS("DS2_5AB",groupe_5AB,4)
DS2_4A=commun.TheDS("DS2_4A",groupe_4A,1)

jeveux=DS2_5AB
jeveux.write_the_file()

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename=jeveux.tex_filename
myRequest.ok_filenames_list=jeveux.ok_filenames_list()