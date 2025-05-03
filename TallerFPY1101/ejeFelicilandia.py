'''
Entrada a Felicilandia 
Valor Entradas:
Niños de hasta 10 años: $2000
Jóvenes de hasta 17 años: $5000
Adultos de hasta 64 años: $7500
Adulto Mayor de 65 años en adelante: $1000

Si pertenece a la Caja Cordillera tiene 15% de descuento
No hay cobro para menores de 3 años
'''
subTotal = 0
edad = int(input('Ingrese su edad: '))
if edad < 3:
    print('Entrada Liberada')
elif 3<= edad <= 10: # edad >= 3 and edad <= 10 : Niños de hasta 10 años: $2000
    subTotal = 2000
elif edad <= 17:
    subTotal = 5000
elif edad <= 64:
    subTotal = 7500
else:
    subTotal = 1000
cantidad = int(input('Ingrese cantidad de entradas: '))
if cantidad > 0 and edad >= 3:
    total = cantidad * subTotal
    print(f'El valor es ${subTotal} por c/u')
    print(f'Total por {cantidad} de entrada(s): ${total}')
    resp = input('¿Pertenece a la Caja Cordillera? (s/n): ').lower()
    if resp == 's':
        print('Tiene descuento!!')
        print('Total a pagar: $', total - (total * 0.15))
    else:
        print('No tiene descuento :(')
else:
    print('Menores de 3 años deben ingresar con un adulto\nCantidad de entradas debe ser Mayor a CERO')
