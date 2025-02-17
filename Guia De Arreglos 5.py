A = [1,3,5,1,3,1]

minimo = min(A)

posiciones =  [i for i, valor in enumerate(A) if valor == minimo]

print("El valor minimo", minimo, "aparece en las posiciones", posiciones)