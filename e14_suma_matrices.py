# Programa para sumar matrices
# Importamos los módulos
import random

#Variables y lógica
numero_matrices = int(input('¿Cuántas matrices quieres sumar?: '))

if numero_matrices > 1:
    rows = int(input('¿Cuántas filas tendrán las matrices?: '))
    columns = int(input('¿Cuántas columnas tendrán las matrices?: '))

    matrix_list = []

    # Llenado de matrices
    for number in range(numero_matrices):
        matrix = []
        for row in range(rows):
            new_row = []
            for column in range(columns):
                new_row.append(random.randint(0, 100))
            matrix.append(new_row)
        matrix_list.append(matrix)
    
    # Suma las matrices
    matrix = []
    for row in range(rows):
        new_row = []
        for column in range(columns):
            sum_matrix = 0
            for matrix_position in range(len(matrix_list)):
                sum_matrix += matrix_list[matrix_position][row][column]
            new_row.append(sum_matrix)
        matrix.append(new_row)
    matrix_list.append(matrix)

    # Imprimir las matrices
    for matrix_row in range(rows):
        for matrix_list_position in range(len(matrix_list)):
            if matrix_row != 1:
                print(f'{matrix_list[matrix_list_position][matrix_row]}', end='   ')
            else:
                if matrix_list_position < len(matrix_list) - 2:
                    print(f'{matrix_list[matrix_list_position][matrix_row]}', end=' + ')
                elif matrix_list_position < len(matrix_list) - 1:
                    print(f'{matrix_list[matrix_list_position][matrix_row]}', end=' = ')
                else:
                    print(f'{matrix_list[matrix_list_position][matrix_row]}', end='   ')
        print()
else:
    print('Se necesitan dos o más matrices para realizar la suma.')