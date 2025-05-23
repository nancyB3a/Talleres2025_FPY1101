cantPersonas = 0
#ciclo de validación de ingreso de cantidad de personas
while cantPersonas < 1:
    try:
        cantPersonas = int(input('Ingrese cant. de personas que han rendido las pruebas de conducir: '))
        if cantPersonas < 1:
            print('Debe ingresar un número mayor a cero!!!')
    except:
        print('Cantidad debe ser un número!!')
#acá estoy segura de tener cantPersonas válido y en el rango
contAprobado = 0 #3 exámenes rendidos
contIncompleto = 0 #menos de 3 exámenes rendidos
#ciclo for para preguntar cantPersonas veces por sus exámenes
for i in range(cantPersonas):
    #ciclo para validar la entrada de exámenes rendidos
    noValido = True
    while noValido:
        try:
            examRendidos = int(input(f'Ingrese cantidad de exámenes rendidos de persona N°{i+1}: '))
            noValido = False
        except:
            print('Exámenes rendidos debe ser un número!!')
    if examRendidos >= 3:
        print('Curso Aprobado, Exámenes Completos!!')
        contAprobado += 1  #equivalente a: contAprobado = contAprobado + 1
    else:
        print('Curso no aprobado, Exámenes Incompletos')
        contIncompleto += 1
#mostrar el detalle de las cantidades
print(f'Se ingresaron {contAprobado} personas Aprobadas con Exámenes completos')
print(f'Se ingresaron {contIncompleto} personas No Aprobadas con Exámenes incompletos')