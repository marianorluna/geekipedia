print('*****************************************')
print('*  Programa que define el mayor número  *')
print('*****************************************\n')


# Definimos las variables
num1 = float(input('Por favor, introduce el primer número: '))
num2 = float(input('Por favor, introduce el segundo número: '))
num3 = float(input('Por favor, introduce el número número: '))


# Definimos la lógica del programa
if num1 > num2 and num1 > num3:
    print(f'\nEl número {num1} es el mayor de los tres.')
else:
    if num2 > num3:
        print(f'\nEl número {num2} es el mayor de los tres.')
    else:
        print(f'\nEl número {num3} es el mayor de los tres.')