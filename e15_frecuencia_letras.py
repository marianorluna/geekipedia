# Programa que cuenta la frecuencia de las letras en un diccionario
string = input('Ingresa un texto: ')

# Crear el diccionario con el texto ingresado
letters = dict.fromkeys(string, 0)

# Recorrer el diccionario
for letter in string:
    letters[letter] += 1
print(letters)
