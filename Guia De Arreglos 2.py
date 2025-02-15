arreglo = []

for i in range(10):
    valor = int(input(f"Ingrese el valor del componente {i+1} :"))
    arreglo.append(valor)

print("La cuarta componente del arreglo es:", arreglo[3])

arreglo.reverse()

print("Los componentes de manera invertida son:", arreglo)

producto = arreglo[0] * arreglo[9]

print("El producto entre el primer y ultimo componente es:", producto)

print("Los componentes de indice impar son:")
for i in range(1, len(arreglo), 2):
    print(f"Indice {i}: {arreglo[i]}")

suma = arreglo[0] + arreglo[2] + arreglo[4] + arreglo[6] + arreglo[8]

print("La suma de los componenetes de indice par es:", suma)

multiplicacion = arreglo[1] * arreglo[3] * arreglo[5] * arreglo[7] * arreglo[9]

print("La multiplicacion de los componentes de indice impar es:", multiplicacion)

auxiliar = arreglo[0]

arreglo[0] = arreglo[9]

arreglo[9] = auxiliar

print("Luego de intercambiar el primer con el ultimo componente queda:", arreglo)