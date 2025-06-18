''' Hacer una app. que permita registrar alumnos con su puntaje PAES y 
hacer el siguiente menú 
1.- Ingresar Estudiante [nombre, rut y tres puntajes PAES] 
2.- Ver puntaje PAES de un estudiante [buscar por nombre] 
3.- Sacar ponderación PAES de un estudiante [buscar por RUT] 
4.- Eliminar un estudiante 
5.- Modificar un puntaje 

Ponderaciones: 
    Primer pje : 40% 
    Segundo pje: 40% 
    Tercer pje: 20% 

Trabaje con funciones (todas las que necesite) 
*recomiendo para puntajes PAES trabajar con una lista dentro de la lista de cada estudiante 
*utilice el rut como la clave del diccionario de estudiantes 
Estudiantes { 
    Rut_1 : [nombre, [pj1, pj2, pj3]], 
    Rut_2 : [nombre, [pj1, pj2, pj3]]
    … 
    } 
'''
import fncTarea as fc
#creo un diccionario con el que trabajaré durante todo el programa
estudiantes = {}
op = ''
while op != '6':
    op = fc.menu()
    if op == '6':
        print('Programa Finalizado!!!')
    elif op == '1': #Ingresar Estudiante [nombre, rut y tres puntajes PAES]
        print('Ingreso de Estudiantes')
        estudiantes = fc.ingresoEstudiante(estudiantes)
        print(estudiantes)
    elif op == '2':
        print('Ver puntaje PAES de un estudiante')
        fc.mostrarPjeAlumno(estudiantes)
    elif op == '3':
        print('Sacar ponderación PAES de un estudiante [buscar por RUT]')
        fc.calcularPonderacion(estudiantes)
    elif op == '4': #Eliminar un estudiante
        print('Eliminar un estudiante')
        estudiantes = fc.eliminarEstudiante(estudiantes)
        print(estudiantes)
    elif op == '5':
        print('Modificar un puntaje de un estudiante')
        fc.modificarUnPje(estudiantes)
        print(estudiantes)
    else:
        print('Opción NO Existe!!')
    
