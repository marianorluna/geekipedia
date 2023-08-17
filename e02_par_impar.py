print('*****************************************************')
print('*  Programa que define si el número es par o impar  *')
print('*****************************************************\n')


# Definimos las variables
numero = int(input('Por favor, introduce un número entero: '))


# Definimos la lógica del programa
if numero % 2 == 0:
    print(f'El número {numero} es par.')
elif numero % 2 == 1:
    print(f'El número {numero} es impar.')
else:
    print('No has introducido un número válido.')
