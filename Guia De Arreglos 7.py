def interseccion_arreglos(arreglo1, arreglo2):
    
    set1 = set(arreglo1)
    
    set2 = set(arreglo2)
    
    interseccion = set1.intersection(set2)
    
    return list(interseccion)
    
N = int(input("Ingrese el numero de elementos en el primer arreglo:"))

arreglo1 = []

print(f"Ingrese {N} valores para el primer arreglo:")

for i in range(N):
    numero = int(input(f"Ingrese el valor de la posicion {i+1}:"))
    arreglo1.append(numero)

M = int(input("Ingrese el numero de elementos en el segundo arreglo:"))

arreglo2 = []

print(f"Ingrese {M} valores para el segundo arreglo:")

for i in range(M):
    numero = int(input(f"Ingrese el valor de la posicion{i+1}:"))
    arreglo2.append(numero)

resultado_interseccion = interseccion_arreglos(arreglo1, arreglo2)

if resultado_interseccion:
    print("La interseccion entre los dos arreglos es:", resultado_interseccion)
else:
    print("No hay elementos en comun entre los arreglos")