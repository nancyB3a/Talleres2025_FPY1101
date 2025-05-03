contA = 0
contB = 0
contError = 0
print('Opción A')
print('Opción B')
opc = input('Ingrese su opción: ').upper() #transforma el texto en mayúscula
if opc == 'A' or opc == 'a':
    contA = contA + 1
    print('Eligió A')
elif opc == 'B':
    contB = contB + 1
    print('Eligió B')
else:
    contError = contError + 1
    print('Opción No existe')
#segunda vez
print('Opción A')
print('Opción B')
opc = input('Ingrese su opción: ').upper() #transforma el texto en mayúscula
if opc == 'A' or opc == 'a':
    contA = contA + 1
    print('Eligió A')
elif opc == 'B':
    contB = contB + 1
    print('Eligió B')
else:
    contError = contError + 1
    print('Opción No existe')
#tercera vez
print('Opción A')
print('Opción B')
opc = input('Ingrese su opción: ').upper() #transforma el texto en mayúscula
if opc == 'A' or opc == 'a':
    contA = contA + 1
    print('Eligió A')
elif opc == 'B':
    contB = contB + 1
    print('Eligió B')
else:
    contError = contError + 1
    print('Opción No existe')

print(f'Opción A seleccionada {contA} vez(ces)')
print(f'Opción B seleccionada {contB} vez(ces)')
print(f'Error seleccionada {contError} vez(ces)')