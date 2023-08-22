# Programa para crear matriz
# Creamos las variables
num_filas = int(input('¿Cuántas filas tendrá la matriz: '))
num_columnas = int(input('¿Cuántas columnas tendrá la matriz: '))
matrix = []
filas = list(range(num_filas))  # No hace falta crear la variable, sólo el range
columnas = list(range(num_columnas))    # No hace falta crear la variable

# Crea la matriz con filas y columnas
for row in filas:
    rows = []
    for element in columnas:
        rows.append(int(input(f'Introduce un elemento a la fila {row}: ')))
    matrix.append(rows)

# Imprime la matriz en formato filas
for row in matrix:
    print(row)