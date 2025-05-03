#esto es un comentario de una línea
#escribir
print('Esto es una impresión por pantalla')
#leer x = input()
sede = input('De que SEDE eres?: ')
print('Yo soy de Viña, mucho gusto estudiante de sede: ', sede)

num = 7 #int
letra = 'hola' #str
existe = True #boolean
otroNum = 3.56 #float

nacimiento = int(input('Ingresa año de nacimiento: ')) 
edad = 2025 - nacimiento
print(f'tienes {edad} años.')


print('Opción A')
print('Opción B')
opc = input('Ingrese su opción: ').upper() #transforma el texto en mayúscula
if opc == 'A' or opc == 'a':
    print('Eligió A')
elif opc == 'B':
    print('Eligió B')
else:
    print('Opción No existe')




