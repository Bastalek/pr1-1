import os

def crea_dir(directorio):
	if os.access(directorio,0):
		return 1
	else:
		os.mkdir(directorio)
		return 0

def lista_fic(directorio):
	if not os.access(directorio,0):
		print 'Directorio inexistente'
		exit()
	lista=os.listdir(directorio)
	for fichero in lista:
		f1=directorio+'/'+fichero
		if os.path.isfile(f1):
			print fichero + '--->'+str(os.path.getsize(f1))

def lista_tam(directorio,tam):
	if not os.access(directorio,0):
		print 'Directorio inexistente'
		exit()
	if tam[-1].upper() not in ('K','M','G'):
		print 'Solo puede ser K,M,G'
		exit()
	t=int(tam[:-1])
	print t
	if tam[-1]=='K':
		t=t*1024
	elif tam[-1]=='M':
		t=t*1024*1024
	else:
		t=t*1024*1024*1024
	lista=os.listdir(directorio)
	print t	
	for fichero in lista:
		f1=directorio+'/'+fichero
		if os.path.isfile(f1):
			if os.path.getsize(f1)>t:
				print fichero + '--->'+str(os.path.getsize(f1))
