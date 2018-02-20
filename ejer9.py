#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Recorrer una tupla con el bucle while

import os

directorio=raw_input('Dime el directorio:')
letra=raw_input('Dime la letra a buscar:')

if not  os.access(directorio,0):
	print "El directorio no existe"
	exit()

ficheros=os.listdir(directorio)

for fichero in ficheros:
	if fichero.count(letra)>0:
		print fichero




