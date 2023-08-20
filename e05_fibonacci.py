# Serie de fibonacci hasta el número 1597
# Declaramos variables en un línea
x, y = 0, 1


# Definimos lógica bucle while
# Funciona igual si en la condición ponemos x o y
while y <= 1597:
    print(x, y, end=' ')
    x = x + y
    y = y + x
