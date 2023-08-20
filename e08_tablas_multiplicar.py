# Programa que genera las tablas de multiplicar:
num_tabla = int(input('¿Qué tabla de multiplicar quieres ver?: '))
for i in range(11):
    print(f'{num_tabla} x {str(i).rjust(2, "0")} = {str(num_tabla * i).rjust(2, "0")}')
