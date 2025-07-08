def menu():
    print("""
    \t***MENÚ***
    1.Cantidad de modelos por marca
    2.Cantidad de patines disponibles por marca
    3.Cantidad de patines disponible por talla
    4.Búsqueda por rango de precio
    5.Búsqueda de patines por tamaño de rueda
    6.Actualizar precio y/o cantidad
    7.Salir
    """)
    op = input('Ingrese su opción: ')
    return op

#Cantidad de modelos por marca
def cantidadModelosXMarca(diccPatines):
    contador = 0
    marca = input('Ingrese marca que desea buscar: ')
    for lista in diccPatines.values():
        if marca.lower() == lista[0].lower():
           contador += 1 
    #fuera del ciclo veo si contó algo
    if contador != 0:
        print(f'Hay {contador} modelo(s) de la marca {marca}.')   
    else:
        print(f'No tenemos disponibles modelo de la marca {marca}.')

#2.Cantidad de patines disponibles por marca
def cantidadPatinesXMarca(diccPat, diccInv):
    totalPatines = 0
    marca = input('Ingrese marca que desea buscar: ')
    for clave, valor in diccPat.items():
        if marca.lower() == valor[0].lower():
            totalPatines += diccInv[clave][1]   
    #fuera del ciclo veo si contó algo
    if totalPatines != 0:
        print(f'Hay {totalPatines} patines de la marca {marca}.')   
    else:
        print(f'No tenemos disponibles patines de la marca {marca}.')

#3.Cantidad de patines disponible por talla
def cantidadPatinesXTalla(diccPat, diccInv):
    totalPatines = 0
    talla = validaNro(int,'Ingrese talla: ','Talla Fuera de rango [21 - 55]','Error: Talla es un número.',21,55)
    for clave, valor in diccPat.items():
        if talla == valor[1]:
            totalPatines += diccInv[clave][1] 
    #fuera del ciclo veo si contó algo
    if totalPatines != 0:
        print(f'Hay {totalPatines} patines de la talla {talla}.')   
    else:
        print(f'No tenemos disponibles patines de la talla {talla}.')

#4.Búsqueda por rango de precio
def buscarXRangoPrecio(diccPat, diccInv):
    encontrado = False
    pMin = validaNro(int, 'Ingrese precio mínimo: ','Precio debe ser Mayor a CERO', 'Precio es un número',0)
    pMax = validaNro(int, 'Ingrese precio máximo: ','Precio debe ser Mayor ' + str(pMin), 'Precio es un número',pMin)
    for clave, valor in diccInv.items():
        if valor[0] >= pMin and valor[0] <= pMax:
            print(f'Valor Patín: ${valor[0]} - {diccPat[clave]}')
            encontrado = True
    if  not encontrado:
        print('No se encontraron patines en el rango de precio.')


#5.Búsqueda de patines por tamaño de rueda
def buscarPorRueda(diccPat):
    encontrado = False
    rueda = validaNro(int, 'Ingresa tamaño de rueda: ', 'Tamaño fuera de rango [30 - 100].', 'Tamaño es un número', 30, 100)
    for lista in diccPat.values():
        if rueda == lista[3]:
            print(lista)
            encontrado = True
    if  not encontrado:
        print('No se encontraron patines con ese diametro de rueda.')


#6.Actualizar precio y/o cantidad
def actualizar(diccInventario):
    existe = True
    opcion = validaNro(int,'1.- Actualizar Precio\n2.- Actualizar Cantidad\n--> ', 
                       'Opción NO existe.', 
                       'Opción es un número',
                       1,2)
    
    while existe:
        codigo = input('Ingrese Código: ')
        if codigo.upper() in diccInventario:
            existe = False
        else:
            print('Código de producto NO Existe!!')

    if opcion == 1: #precio
        newPrecio = validaNro(int,'Ingrese nuevo precio: ', 'Precio debe ser mayor a CERO', 'Precio es un número',1)
        diccInventario[codigo][0] = newPrecio
        print('Precio Actualizado')
    else:
        newCant = validaNro(int, 'Ingrese nueva cantidad: ', 'Cantidad No puede ser Negativo', 'Cantidad es un número', 0)
        diccInventario[codigo][1] = newCant
        print('Cantidad Actualizada')
    return diccInventario
        
#función para validad números
def validaNro(tipo, txtIn, txtError, txtExep, vMin=None, vMax=None):
    repite = True
    while repite:
        try:
            nro = tipo(input(txtIn))
            if vMin != None and vMax != None:
                if nro >= vMin and nro <= vMax:
                    repite = False
                else:
                    print(txtError)
            elif vMin != None:
                if vMin <= nro:
                    repite = False
                else:
                    print(txtError)
            elif vMax != None:
                if vMax >= nro:
                    repite = False
                else:
                    print(txtError)
            else:
                repite = False
        except:
            print(txtExep)
    return nro
