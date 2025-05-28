Mayor_10 = 0
Menor_10 = 0
Años_Antiguedad = 0
NombreEmpleado = ""
while True:
    try:
        cantidadEmpleado = int(input("Ingrese la cantidad de empleados: "))
    except ValueError:
        print("Solo numero enteros!!") 

        for i in range(cantidadEmpleado):
         
         NombreEmpleado = input("Ingrese el nombre del empleado: ")  
        
        Años_Antiguedad = int(input("Ingrese los años de antiguedad: "))
    except ValueError:
        print("Debe ingresar un numero entero...")
        continue
    if Años_Antiguedad >= 10:
        Años_Antiguedad += Mayor_10
        Años_Antiguedad = Mayor_10
    else:
        Años_Antiguedad += Menor_10
        Años_Antiguedad = Menor_10

print(f"Se registraron {Mayor_10} empleados con mas de 10 años de antiguedad")
print(f"Se registraron {Menor_10} empleados con mas de 10 años de antiguedad")
        