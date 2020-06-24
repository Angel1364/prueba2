import random
fil=int(input("Ingrese el numero de filas : "))
col=int(input("Ingrese el numero de columnas : "))

a=[[random.randint (1,10) for i in range(fil)] for j in range(col)] 
print("Salidas de datos aleatorios")
for f in a:
    print(f)