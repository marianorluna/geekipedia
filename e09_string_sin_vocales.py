# Programa que elimina vocales de un string y lo devuelve
frase = input('Introduce una frase: ')
letra = input('¿Con qué letra deseas terminar el bucle?: ')


for character in frase:
    # Este condicional detendría el bucle, si encuentra una coincidencia
    if character.lower() == letra.lower():
        break
    # A partir de acá elimina las vocales
    # Usamos el método lower de manera temporal
    elif character.lower() == 'a':
        continue
    elif character.lower() == 'e':
        continue
    elif character.lower() == 'i':
        continue
    elif character.lower() == 'o':
        continue
    elif character.lower() == 'u':
        continue
    # El parámetro end elimina salto de línea
    print(character, end='')
