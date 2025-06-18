def menu():
    print('\tMenú')
    print('~'*15)
    print("""
    1.- Ingresar Estudiante [nombre, rut y tres puntajes PAES] 
    2.- Ver puntaje PAES de un estudiante [buscar por nombre] 
    3.- Sacar ponderación PAES de un estudiante [buscar por RUT] 
    4.- Eliminar un estudiante 
    5.- Modificar un puntaje Ponderaciones
    6.- Salir
    """)
    opcion = input('Ingrese su opción: ')
    return opcion

def ingresoEstudiante(unDicc):
    #RUT
    while True:
        rut = input('Ingrese rut del estudiante: ')
        if rut not in unDicc:
            break
        else:
            print('Estudiante YA existe, ingrese uno nuevo!!')
    #nombre
    while True:
        nombre = input('Ingrese nombre del estudiante: ')
        if nombre.isalpha():
            break
        else:
            print('Nombre admite sólo letras')
    #puntajes
    listaPjes=[]
    for i in range(3):
        ptos = 0
        while ptos < 100 or ptos > 1000:
            try:
                ptos = int(input(f'Ingrese puntaje prueba n°{i+1}: '))
                if ptos < 100 or ptos > 1000:
                    print('Error: Fuera de rango [100-1000].')
            except:
                print('Puntaje es un número entero.')
        listaPjes.append(ptos)
    #tengo todos los input: lo s grabo en el diccionario
    unDicc[rut] = [nombre,listaPjes]
    print('Estudiante Creado Con Exito!!')
    return unDicc

def mostrarPjeAlumno(elDicc):
    #nombre
    while True:
        nombre = input('Ingrese nombre del estudiante: ')
        if nombre.isalpha():
            break
        else:
            print('Nombre admite sólo letras')
    existe = False
    for _clave,valor in elDicc.items():
        if valor[0].upper() == nombre.upper():
            print(f'RUT: {_clave} - Puntajes: {valor[1]}')
            existe = True
    if not existe:
        print('NO hay estudiantes con ese nombre.')

def calcularPonderacion(unDiccionario):
    #RUT
    while True:
        rut = input('Ingrese rut del estudiante: ')
        if rut not in unDiccionario:
           print('Estudiante NO existe, ingrese uno nuevo!!')   
        else:
            break
    unaLista = unDiccionario[rut]
    ponderado = 0
    '''for i in range(3):
        if i == 0:
            ponderado = unaLista[1][i] * 0.4
        elif i == 1:
            ponderado += unaLista[1][i] * 0.4
        elif i == 2:
            ponderado += unaLista[1][i] * 0.2'''

    ponderado = unaLista[1][0] * 0.4
    ponderado += unaLista[1][1] * 0.4
    ponderado += unaLista[1][2] * 0.2

    print('Puntaje Ponderado:', round(ponderado))             

def eliminarEstudiante(unDicc):
    #RUT
    while True:
        rut = input('Ingrese rut del estudiante: ')
        if rut not in unDicc:
           print('Estudiante NO existe, ingrese uno nuevo!!')   
        else:
            break
    del unDicc[rut]
    print('Estudiante eliminado con Exito')
    return unDicc

def modificarUnPje(elDicc):
    #RUT
    while True:
        rut = input('Ingrese rut del estudiante: ')
        if rut not in elDicc:
           print('Estudiante NO existe, ingrese uno nuevo!!')   
        else:
            break
    nro = 0
    while nro < 1 or nro > 3:
        try:
            nro=int(input('Ingrese número de prueba que desea modificar [1-3]: '))
            if nro < 1 or nro > 3:
                print('Nro de prueba Fuera de Rango')
        except:
            print('N° de prueba DEBE ser numérico!!')
    ptos = 0
    while ptos < 100 or ptos > 1000:
        try:
            ptos = int(input(f'Ingrese nuevo puntaje: '))
            if ptos < 100 or ptos > 1000:
                print('Error: Fuera de rango [100-1000].')
        except:
            print('Puntaje es un número entero.')
    elDicc[rut][1][nro-1] = ptos
    print('Puntaje Modificado')
    return elDicc
