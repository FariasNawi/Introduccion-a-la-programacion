n = int(input("Ingrese el numero de componentes del vector:"))

vector = []
    
for i in range(n):
        valor = int(input(f"Ingrese el valor del componente {i+1} :"))
        vector.append(valor)
    
print("El vector ingresado es:", vector)