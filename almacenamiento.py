def maximizar(As, D):
	ordenados=[]
	tam=0
	As.sort(key=lambda x: x[1])
	for i in range (len(As)):
		if tam+As[i][1] < D:
			ordenados.append(As[i])
			tam=tam+As[i][1]
	return ordenados