# Programa que elimina caracteres contínuos
lista = ['A', 'B', 'b', 'c', 'E', 'E', 'f']
print(f'Lista original: {lista}')
elemento_eliminar = input('Introduce el elemento que deseas eliminar: ')

for _ in lista:
    if elemento_eliminar.lower() in lista:
        lista.remove(elemento_eliminar.lower())
    elif elemento_eliminar.upper() in lista:
        lista.remove(elemento_eliminar.upper())

print(f'Elemento eliminado: {lista}')
