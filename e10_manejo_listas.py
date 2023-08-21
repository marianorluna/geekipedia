# Programa para el manejo de listas
longitud_lista = int(input('¿Cuántos números enteros contendrá la lista?: '))
lista = []
for _ in range(longitud_lista):
    num = int(input('Introduce un número entero: '))
    lista.append(num)
print(f'Lista: {lista}')
print(f'La suma total de los elementos es: {sum(lista)}')
