# Programa que modifica una tupla
tupla = (5, 8, 3, 3, 1, 6, 2)
print(f'Tupla original: {tupla}')
numero = int(input('¿Cuál de estos números quieres modificar por cero: '))

tupla_modificada = list(tupla)
len_tupla_modificada = len(tupla_modificada)

for num in range(len_tupla_modificada):
    if tupla_modificada[num] == numero:
        tupla_modificada[num] = 0

tupla = tuple(tupla_modificada)
print(f'Tupla modificada: {tuple(tupla)}')
