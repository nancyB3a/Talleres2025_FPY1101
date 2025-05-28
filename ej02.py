entradas = 50

while True:
    try:
        print("*****Cine Estrella*****")
        print(" Bienvenido al sistema de ventas de entradas del cine Estrella")
        print("1. Ver cuantas entradas quedan")
        print("2. Comprar una cantidad de entradas")
        print("3. Salir del sistema")
    except ValueError:
        print("Opcion no valida Por favor, seleccione una opcion del 1 al 3")
        opcion = input("Seleccione una opcion: ")
    
        

    try:
     if opcion == 1:
         print(f"Entradas disponibles: {entradas}")
         continue
          

     elif opcion == 2:
         comprarEntra = int(input("¿Cuantas entradas desea comprar?: "))
         entradas -= comprarEntra
    except ValueError:
         print("Debe ingresar un numero valido.")

        
         if opcion == 3:
          print("Gracias por usar el sistema de ventas del Cine Estrella ¡Hasta pronto!")
else:
   print("Opcion no valida Por favor, seleccione una opcion del 1 al 3")           
   
