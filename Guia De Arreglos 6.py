def obtener_top_10(arreglo):
    
    arreglo_ordenado = sorted(arreglo, reverse = True)
    
    Top_10 = arreglo_ordenado[:10]
    
    print("Ranking de los 10 numeros mas grandes:")
    for i, numero in enumerate(Top_10, 1):
        print(f"{i}.{numero}")

N = int(input("Ingrese el número de elementos en el arreglo:"))

arreglo = []

for i in range(N):
    numero = int(input(f"Ingrese el valor para la posicion {i+1}:"))
    arreglo.append(numero)

obtener_top_10(arreglo)

