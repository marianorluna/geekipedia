print('Calculadora con una sola variable:\n')
print('**********************')
print('*  Menú de opciones  *')
print('**********************')
print('''
1. Suma
2. Resta
3. Multiplicación
4. División
5. División entera
6. Exponente
7. Módulo o resto
''')


opcion = int(input('Introduce la opción deseada: '))


if opcion == 1:
    print('Elegiste suma\n')
    num1 = int(input('Introduce el primer número: '))
    num1 += int(input('Introduce el primer número: '))
    print(f'El resultado de la suma es {num1}')
elif opcion == 2:
    print('Elegiste resta')
    num1 = int(input('Introduce el primer número: '))
    num1 -= int(input('Introduce el primer número: '))
    print(f'El resultado de la resta es {num1}')
elif opcion == 3:
    print('Elegiste multiplicación')
    num1 = int(input('Introduce el primer número: '))
    num1 *= int(input('Introduce el primer número: '))
    print(f'El resultado de la multiplicación es {num1}')
elif opcion == 4:
    print('Elegiste división')
    num1 = float(input('Introduce el primer número: '))
    num1 /= float(input('Introduce el primer número: '))
    print(f'El resultado de la división es {round(num1, 2)}')
elif opcion == 5:
    print('Elegiste división entera')
    num1 = int(input('Introduce el primer número: '))
    num1 //= int(input('Introduce el primer número: '))
    print(f'El resultado de la división entera es {num1}')
elif opcion == 6:
    print('Elegiste exponente')
    num1 = int(input('Introduce el primer número: '))
    num1 **= int(input('Introduce el primer número: '))
    print(f'El resultado de la potencia es {num1}')
elif opcion == 7:
    print('Elegiste módulo o resto')
    num1 = int(input('Introduce el primer número: '))
    num1 %= int(input('Introduce el primer número: '))
    print(f'El resultado del módulo o resto es {num1}')
else:
    print('No elegiste una opción válida')
