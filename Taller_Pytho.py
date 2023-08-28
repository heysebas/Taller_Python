# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# grupo
# Johan Sebastian Grisales montoya
# Daniela Villalba Torres


# 1. (1.25 puntos) Escriba un programa en Python que acepte una cadena y calcule una metrica que sea el
# numero total de caracteres de la cadena multiplicado por el numero total de vocales que contiene. Se deben
# tener en cuenta las vocales en may´uscula y tildadas.
# Entrada: Hola A Todos los Estudiantes del sal´on!
# Salida: 546
# Se debe usar: cadenas, funciones con cadenas
# No se debe usar: ciclos, condicionales.


palabra = input("Ingrese una cadena: ")

palabra = palabra.lower()

metrica = palabra.count('a') + palabra.count('e') + \
          palabra.count('i') + palabra.count('o') + \
          palabra.count('u') + palabra.count('á') + \
          palabra.count('é') + palabra.count('í') + \
          palabra.count('ó') + palabra.count('ú')

print(f'{metrica*len(palabra)}')
