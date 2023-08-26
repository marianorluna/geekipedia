# Programa que valida e imprime valor
tupla = ('Ana', 'Gerardo', 'María', 'Carlos', 'Valentina')
print(tupla)
len_tupla = len(tupla) - 1

validator = 0
while validator == 0:
    num = int(input(f'\nIntroduce un número entero entre 0 y {len_tupla}: '))
    if 0 <= num <= len_tupla:
        print(f'\nEl nombre es: {tupla[num]}')
        validator = 1
    else:
        print('¡Error!: Número inválido, vuelve a intentar.')
