def maximizar(As, D):
	ordenados=[]
	tam=0
	As.sort(key=lambda x: x[1])
	for i in As:
		if tam+i[1] < D:
			ordenados.append(i)
			tam=tam+i[1]
	return ordenados


"""

As = [('archivo1', 10), ('archivo2', 5), ('archivo3', 3),
              ('archivo4', 8), ('archivo5', 9), ('archivo6', 1)]
D=10

maximizar(As,D)
"""