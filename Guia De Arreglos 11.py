curso_A = [160, 155, 170, 180, 165, 175, 168, 162, 173, 158, 169, 171, 174, 166, 159, 178, 167, 176, 172, 164]

curso_B = [158, 165, 172, 160, 169, 177, 168, 181, 174, 162, 171, 163, 175, 167, 159, 176, 170, 164, 168, 173]

max_A = max(curso_A)

max_B = max(curso_B)

pos_A = curso_A.index(max_A) + 1

pos_B = curso_B.index(max_B) + 1

print(f"Estatura maxima del curso A: {max_A} cm, alumno en la posicion: {pos_A}")

print(f"Estatura maxima del curso B: {max_B} cm, alumno en la posicion: {pos_B}")

if max_A > max_B:
    print("La estatura máxima del curso A es mayor.")
    
elif max_B > max_A:
    print("La estatura máxima del curso B es mayor.")
    
else:
    print("Las estaturas máximas de ambos cursos son iguales.")
