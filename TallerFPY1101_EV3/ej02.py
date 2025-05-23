velMin = 201
velMax = 0
contador = 0
opc = '0'
acumVelocidad = 0
while opc != '4':
    print('*** Menú Principal ***')
    print("""
    1. Registrar velocidad del vehículo.
    2. Mostrar velocidad mínima y máxima registrada.
    3. Mostrar velocidad promedio registrada.
    4. Terminar programa.""")
    opc = input('-->')
    if opc == '1': #1. Registrar velocidad del vehículo. [10 y 200]
        velocidad = 0
        while velocidad < 10 or velocidad > 200:
            try:
                velocidad = int(input('Ingrese velocidad observada [entre 10 y 200]: '))
                if velocidad < 10 or velocidad > 200:
                    print('Debe ingresar un número entre 10 y 200!!')
            except:
                print('Debe ingresar un número entero!!')
        #acá tengo velocidad numérica y en el rango
        if velocidad > velMax:
            velMax = velocidad
        if velocidad < velMin:
            velMin = velocidad
        acumVelocidad += velocidad
        contador += 1
        print('Velocidad registrada con Exito!!')
    elif opc == '2': #2. Mostrar velocidad mínima y máxima registrada.
        if contador != 0:
            print(f'Velicidad Mínima Registrada: {velMin} km/h')
            print(f'Velicidad Máxima Registrada: {velMax} km/h')
        else: 
            print('Aún no se han registrado velocidades!!')    
    elif opc == '3': #3. Mostrar velocidad promedio registrada.
        if contador != 0:
            promedio = acumVelocidad/contador
            #print(f'Promedio de Velocidad: {round(promedio,1)} km/h.') Redondear con round
            print(f'Promedio de Velocidad: {promedio:.2f} km/h.')
        else: 
            print('Aún no se han registrado velocidades!!')
    elif opc == '4':
        print('Saliendo del programa....')
    else:
        print('Opción NO Existe!!!')