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

print(
    f'cantidad de caracteres de la palabra es : {len(palabra)} y la cantida de vocales es de: {metrica}  y multiplicado es: {metrica * len(palabra)}')

# 2. (1.25 puntos) Realice un algoritmo que pida al usuario un año entre 1904 y 2196 (Se debe validar que el
# usuario ingrese un numero entero en el intervalo indicado) y luego verifique si es bisiesto o no. Un año es
# bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100, o bien si es divisible entre
# 400.
# Entrada: 2008
# Salida: 2008 es bisiesto
# Se debe usar: cadenas, ciclo while (para la validaci´on), comprobaci´on de tipos de variables, condicionales.
# No se debe usar: ciclo for.


# entrada = int(input('ingrese la fecha de nacimiento: '))
# if (entrada > 1904 & entrada < 2196):
#    if (resul := not entrada % 4 and (entrada % 100 or not entrada % 400)):
#        print('fecha bisiesta', entrada)
#    else:
#        print('fecha no es bisiesta')


while True:
    try:
        entrada = int(input('Ingrese un año entre 1904 y 2196: '))
        if 1904 <= entrada <= 2196:
            if (entrada % 4 == 0 and (entrada % 100 != 0 or entrada % 400 == 0)):
                print(f'{entrada} es un año bisiesto.')
            else:
                print(f'{entrada} no es un año bisiesto.')
            break
        else:
            print('El año debe estar entre 1904 y 2196.')
    except ValueError:
        print('Por favor, ingrese un número válido.')

# 3. (1.25 puntos) Diseña un algoritmo de validación de usuario,
# pidiendo un login y una contraseña y se comparen ambos valores
# con los almacenados en dos constantes. Si el usuario introduce
# correctamente los valores, se muestra el mensaje "Login y contraseña
# correctos" y termina el programa; en caso contrario, se muestra el mensaje
# "Login incorrecto" o "Contraseña incorrecta" o "Login y contraseña incorrectos",
# según corresponda. Se permite repetir el proceso un máximo de tres veces. En caso de i
# ngresar la contraseña incorrecta más de tres veces, se debe mostrar el mensaje "Usuario bloqueado".
# Se deben utilizar: Sentencias vistas hasta la fecha.

user = "admin"
contrasena = "admin"

x = 0

while x < 3:
    login = input("Ingrese el Usuario: ")
    password = input("Ingrese la contraseña: ")

    if login == user and password == contrasena:
        print(f'el nombre del usuario: {login} y la contaseña son correcta')
        break
    else:
        x += 1
        if x == 3:
            print('la cantindad de intento fue superada y la cuenta se bloqueara temporalmente')
            break
        else:
            if login != user:
                print(f'El usuario: {login} es incorrecto')
            if password != contrasena:
                print('La contraseña es incorrecto')

# 4. (1.25 puntos) Programme un algoritmo que solicite al usuario 5 números enteros
# (se debe validar que sean números enteros, positivos o negativos). Luego muestre lo
# siguiente: el valor mínimo, el valor máximo, la suma de los números, el promedio y
# los números ordenados de mayor a menor. No se debe usar: listas, ni otra estructura similar.

minimo = float('inf')
maximo = float('-inf')
suma = 0

for i in range(5):
    while True:
        try:
            num = int(input(f'Ingrese el número {i + 1}: '))
            break
        except ValueError:
            print('Por favor, ingresar un número entero válido.')

    if num < minimo:
        minimo = num
    if num > maximo:
        maximo = num
    suma += num

promedio = suma / 5

print(f'Valor mínimo: {minimo}\nValor máximo: {maximo}\nSuma de los números: {suma}\nPromedio de los números: {promedio}')
