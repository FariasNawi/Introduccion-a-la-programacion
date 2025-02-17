def encontrar_multiplos(arreglo):
    
    menor_multiplo_5 = None
    
    mayor_multiplo_10 = None
    
    pos_menor_5 = -1
    
    pos_mayor_10 = -1
    
    for i, num in enumerate(arreglo):
        if num % 5 == 0:
            if menor_multiplo_5 is None or num < menor_multiplo_5:
                menor_multiplo_5 = num
                pos_menor_5 = i
        if num % 10 == 0:
            if mayor_multiplo_10 is None or num > mayor_multiplo_10:
                mayor_multiplo_10 = num
                pos_mayor_10 = i
    
    if menor_multiplo_5 is not None:
         print(f"El menor multiplo de 5 es {menor_multiplo_5} en la posicion {pos_menor_5}")
    else:
        print("No hay multiplos de 5 en el arreglo")
        
    if mayor_multiplo_10 is not None:
        print(f"El mayor multiplo de 10 es {mayor_multiplo_10} en la posicion {pos_mayor_10}")
    else:
        print("No hay multiplos de 10 en el arreglo")

n = int(input("Ingrese el numero de elementos en el arreglo:"))

arreglo = []

print(f"Ingrese {n} valores para el arreglo:")
for i in range(n):
    numero = int(input(f"Ingrese el valor para la posicion {i+1}:"))
    arreglo.append(numero)

encontrar_multiplos(arreglo)