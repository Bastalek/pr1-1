#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Recorrer una tupla con el bucle while

import os

directorio=raw_input('Dime el directorio:')

if not  os.access(directorio,0):
	print "El directorio no existe"
	exit()

ficheros=os.listdir(directorio)

for fichero in ficheros:
	if fichero[-3:] =='.sh':
		print fichero




