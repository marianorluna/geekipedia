# Programa para invertir un string
my_string = input('Introduce un string para invertirlo: ')
my_string_invertido = ''
for character in my_string:
    my_string_invertido = character + my_string_invertido
print('Este es tu STRING invertido:', my_string_invertido)
