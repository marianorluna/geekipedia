print('\n===================================')
print('    Sistema de control vacacional    ')
print('=====================================\n')


# Definimos las variables
nombre = input('Nombre del solicitante: ')
clave = input('Clave asignada: ')
anios = float(input('Años trabajados: '))


# Definimos la lógica del programa
if clave == '1':
    if anios <= 1:
        print(f'{nombre} le corresponden 6 días de vacaciones.')
    elif anios > 1 and anios < 7:
        print(f'{nombre} le corresponden 14 días de vacaciones.')
    elif anios >= 7:
        print(f'{nombre} le corresponden 20 días de vacaciones.')
    else:
        print(f'{nombre} no tiene derecho a vacaciones aún.')
elif clave == '2':
    if anios <= 1:
        print(f'{nombre} le corresponden 7 días de vacaciones.')
    elif anios > 1 and anios < 7:
        print(f'{nombre} le corresponden 15 días de vacaciones.')
    elif anios >= 7:
        print(f'{nombre} le corresponden 22 días de vacaciones.')
    else:
        print(f'{nombre} no tiene derecho a vacaciones aún.')
elif clave == '3':
    if anios <= 1:
        print(f'{nombre} le corresponden 10 días de vacaciones.')
    elif anios > 1 and anios < 7:
        print(f'{nombre} le corresponden 20 días de vacaciones.')
    elif anios >= 7:
        print(f'{nombre} le corresponden 30 días de vacaciones.')
    else:
        print(f'{nombre} no tiene derecho a vacaciones aún.')
else:
    print('La clave ingresada no existe')

# Mensaje de finalización
print('\nEl programa ha finalizado.\n')