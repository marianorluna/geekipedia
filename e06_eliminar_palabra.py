# Programa para eliminar palabras dentro de frases
frase = input('Introduce una frase: ')
palabra_eliminar = input('Introduce la palabra que quieras eliminar: ')
indice = frase.find(palabra_eliminar)
sub_frase = frase[0: indice] + frase[(indice + len(palabra_eliminar) + 1):]
print('Cadena con palabra eliminada:', sub_frase)
