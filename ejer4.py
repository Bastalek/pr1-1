#!/usr/bin/env python
#-*- coding: utf-8 -*-
#calcular edad
edad=input('Pon tu añio de nacimiento:')
edad=2018-edad
print 'Tu edad es:'+str(edad)
if edad >0 and edad <18:
	print 'Jovencito'
elif edad >=18 and edad <=30:
	print 'Joven'
elif edad >30 and edad <45:
	print 'Maduro'
else:
	print 'viejuno'
