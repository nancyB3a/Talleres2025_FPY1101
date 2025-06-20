def menu():
    print('Menú Biblioteca')
    print('~'*20)
    print("""
    1.- Matricular.
    2.- Cancelar Matrícula.
    3.- Cupos disponibles.
    4.- Salir.""")
    op = input('Ingrese su opción: ')
    return op

#el código de verificación debe tener un largo mínimo de 4 caracteres, incluir al menos 1 letra mayúscula, 
# al menos 1 número y no puede contener espacios.
def validar_codigo_verificacion(codigoVerf):
    tieneMayusculas = any(c.isupper() for c in codigoVerf)
    tieneNro = any(c.isdigit() for c in codigoVerf)
    sinEspacios = ' ' not in codigoVerf
    return len(codigoVerf) >= 4 and tieneMayusculas and tieneNro and sinEspacios

def matricular(diccUsuarios, cuposN, cuposA):
    hayCupos = True
    if cuposN == 0 and cuposA == 0:
        print('No hay cupos disponibles para ninguna categoría.')
        hayCupos = False
        #return diccUsuarios, cuposN, cuposA
    
    if hayCupos:
        #el código del usuario no debe estar repetido y debe tener un largo de 6 caracteres
        while True:
            codigo = input('Ingrese un código (6 caracteres): ').strip()
            if len(codigo) == 6 and codigo not in diccUsuarios:
                break
            else:
                print('Código inválido o ya registrado. Intente Nuevamente')
        #el nombre debe contener sólo letras.
        while True:
            nombre = input('Ingrese nombre del usuario: ')
            if nombre.replace(' ','').isalpha():
                break
            else:
                print('El nombre solo debe contener letras. Intente nuevamente')
        #el tipo de inscripción solo permite “N” (Niños) o “A” (Adultos)
        while True:
            tipo = input('Ingrese tipo de usuario [N: Niños / A: Adultos]: ').upper()
            if tipo == 'N' and cuposN > 0:
                break
            elif tipo == 'A' and cuposA > 0:
                break
            else:
                print('Tipo inválido o sin cupos disponibles. Intente Nuevamente')
        #codigo de verificacion
        while True:
            codigoVerif = input('Ingrese código de verificación: ')
            if validar_codigo_verificacion(codigoVerif):
                break
            else:
                print('Código NO válido. Debe teneer mínimo 4 caracteres, al menos 1 mayúscula, 1 número y sin espacios.')
        #ahora que tengo todo guardo en el diccionario
        diccUsuarios[codigo] = [nombre, tipo, codigoVerif]  
        if tipo == 'N':
            cuposN -= 1
        else:
            cuposA -= 1
        print(f'¡Matrícula registrada con éxito para {nombre}')      
    return diccUsuarios, cuposN, cuposA

def cancelar_matricula(diccUsuarios, cuposN, cuposA):
    codigo = input('Ingrese el código del usuario a cancelar: ').strip()
    if codigo in diccUsuarios:
        tipo = diccUsuarios[codigo][1]
        del diccUsuarios[codigo]
        if tipo == 'N':
            cuposN += 1
        else:
            cuposA += 1
        print('Matrícula Cancelada correctamente!')
    else:
        print('No existe usuario con ese código')
    return diccUsuarios, cuposN, cuposA

def mostrar_cupos(cuposN, cuposA):
    print(f'Hay {cuposN} cupos de niños disponibles.')
    print(f'Hay {cuposA} cupos de adulto disponibles.')

