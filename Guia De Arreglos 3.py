A = [1,2,3,4,5]

B = [6,7,8,9,10]

if len(A) == len(B):
    
    C = [A[i]+B[i] for i in range(len(A))]
    print("El arreglo C es:", C)
else:
    print("Los arreglos A y B deben tener la misma longitud")