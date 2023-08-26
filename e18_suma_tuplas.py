# Programa que suma tuplas
tupla1 = (1, 2, 3, 4, 5)
tupla2 = (8, 6, 4, 2, 0)
tupla3 = []

for x, y in zip(tupla1, tupla2):
    tupla3.append(x + y)

print('Tupla 1:'.ljust(13), tupla1)
print(''.ljust(13), '+')
print('Tupla 2:'.ljust(13), tupla2)
print(''.ljust(13), '===============')
print('Total:'.ljust(13), tuple(tupla3))
