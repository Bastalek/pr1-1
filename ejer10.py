#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pedir el nombre y ponerlo en mayusculao

import sys
if len(sys.argv) != 2:
	print "Falta alguna argumento"
	exit()
print sys.argv[0]
print sys.argv[1]
print "Tu nombre en mayusculas es:" + sys.argv[1].upper()







