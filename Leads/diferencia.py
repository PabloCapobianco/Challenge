def diferencia(lista, listb):
	diferencia = []
	for item in lista:
		if item not in listb:
			diferencia.append(item)
	return diferencia
	 
