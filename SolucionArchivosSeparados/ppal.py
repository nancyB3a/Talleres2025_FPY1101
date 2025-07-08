import funciones as fc

patines = {
'1234PT': ['Rollerblade', 38, 'bota rígida', 80, 'aluminio', 'intermedio', 'negro con rojo', 1.6, 'trasero', 'fitness'],
'4321PT': ['Powerslide', 37, 'bota blanda', 76, 'plástico reforzado', 'principiante', 'azul marino', 1.4, 'trasero', 'fitness'],
'1111PT': ['FR Skates', 39, 'bota rígida', 90, 'aluminio', 'avanzado', 'negro mate', 1.9, 'sin freno', 'urbano'],
'1212PT': ['Oxelo', 40, 'bota blanda', 72, 'plástico', 'principiante', 'gris con verde', 1.3, 'trasero', 'fitness'],
'2121PT': ['Rollerblade', 42, 'bota rígida', 84, 'aluminio', 'intermedio', 'negro con azul', 1.7, 'intercambiable', 'urbano'],
'2222PT': ['Fila', 36, 'bota blanda', 76, 'plástico reforzado', 'principiante', 'rosa con blanco', 1.2, 'trasero', 'fitness'],
'3131PT': ['Oxelo', 41, 'bota semirrígida', 80, 'aluminio', 'intermedio', 'gris con rojo', 1.5, 'trasero', 'fitness'],
'1313PT': ['Oxelo', 40, 'bota rígida', 100, 'aluminio', 'avanzado', 'negro con dorado', 2.0, 'sin freno', 'freestyle']
}
inventario = {
'1234PT': [89990, 10],
'4321PT': [79990, 4],
'1111PT': [139990, 1],
'1212PT': [59990, 13],
'2121PT': [49990, 22],
'2222PT': [99990, 7],
'3131PT': [119990, 4],
'1313PT': [109990, 5]
}

opc = ''
while opc != '7':
    #llamado a fc menu
    opc = fc.menu()
    if opc == '7':
        print('Programa Terminado!!!')
    elif opc == '1':
        print('1.Cantidad de modelos por marca')
        fc.cantidadModelosXMarca(patines)
    elif opc == '2':
        print('2.Cantidad de patines disponibles por marca')
        fc.cantidadPatinesXMarca(patines, inventario)
    elif opc == '3':
        print('3.Cantidad de patines disponible por talla')
        fc.cantidadPatinesXTalla(patines, inventario)
    elif opc == '4':
        print('4.Búsqueda por rango de precio')
        fc.buscarXRangoPrecio(patines, inventario)
    elif opc == '5':
        print('5.Búsqueda de patines por tamaño de rueda')
        fc.buscarPorRueda(patines)
    elif opc == '6':
        print('6.Actualizar precio y/o cantidad')
        inventario = fc.actualizar(inventario)
    else:
        print('Error: Opción NO Existe!!!')
    