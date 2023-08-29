# Grupo de trabajo:
# Johan Sebastian Grisales montoya
# Daniela Villalba Torres


# 1. (1.25 puntos) Escriba un programa en Python que acepte una cadena y calcule una metrica que sea el
# numero total de caracteres de la cadena multiplicado por el numero total de vocales que contiene. Se deben
# tener en cuenta las vocales en mayúscula y tildadas.
# Entrada: Hola A Todos los Estudiantes del salón!
# Salida: 546
# Se debe usar: cadenas, funciones con cadenas
# No se debe usar: ciclos, condicionales.

# palabra = input("Ingrese una cadena: ")
#
# palabra = palabra.lower()
#
# metrica = palabra.count('a') + palabra.count('e') + \
#           palabra.count('i') + palabra.count('o') + \
#           palabra.count('u') + palabra.count('á') + \
#           palabra.count('é') + palabra.count('í') + \
#           palabra.count('ó') + palabra.count('ú')
#
# print(f'La cantidad de caracteres de la palabra es: {len(palabra)} y la cantidad de vocales es de: {metrica} '
#       f'y multiplicando ambas cosas es: {metrica * len(palabra)}')

# 2. (1.25 puntos) Realice un algoritmo que pida al usuario un año entre 1904 y 2196 (Se debe validar que el
# usuario ingrese un numero entero en el intervalo indicado) y luego verifique si es bisiesto o no. Un año es
# bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100, o bien si es divisible entre
# 400.
# Entrada: 2008
# Salida: 2008 es bisiesto
# Se debe usar: cadenas, ciclo while (para la validación), comprobación de tipos de variables, condicionales.
# No se debe usar: ciclo for.

# entrada = input('Ingrese un número entero entre 1904 y 2196: ')
#
# while not entrada.isnumeric():
#     entrada = input('Ingrese un número entero entre 1904 y 2196: ')
#
# entrada = int(entrada)
# while entrada < 1904 or entrada > 2196:
#     entrada = int(input("Ingrese un número entero entre 1904 y 2196: "))
#
# if (entrada % 4 == 0 and not entrada % 100 == 0) or entrada % 400 == 0:
#     print(f'El año {entrada} es bisiesto')
# else:
#     print(f'El año {entrada} no es bisiesto')

# 3. (1.25 puntos) Diseña un algoritmo de validación de usuario,
# pidiendo un login y una contraseña y se comparen ambos valores
# con los almacenados en dos constantes. Si el usuario introduce
# correctamente los valores, se muestra el mensaje "Login y contraseña
# correctos" y termina el programa; en caso contrario, se muestra el mensaje
# "Login incorrecto" o "Contraseña incorrecta" o "Login y contraseña incorrectos",
# según corresponda. Se permite repetir el proceso un máximo de tres veces. En caso de ingresar la contraseña
# incorrecta más de tres veces, se debe mostrar el mensaje "Usuario bloqueado".
# Se deben utilizar: Sentencias vistas hasta la fecha.

#Preguntar duda sobre este ejercicio
# usuario = 'admin'
# contrasena = 'admin'
#
# intentos = 0
# while intentos < 3:
#
#     login = input('Ingrese el usuario: ')
#     password = input('Ingrese la contraseña: ')
#
#     if login == usuario and password == contrasena:
#         print('Login y contraseña correcta')
#         break
#     elif login != usuario and password != contrasena:
#         print('Login y contraseña incorrectos')
#     elif (not login == usuario and password == contrasena):
#         print('Login incorrecto')
#     else:
#         intentos += 1
#         print('Contraseña incorrecta')
# else:
#     print('Usuario bloqueado')

# 4. (1.25 puntos) Programme un algoritmo que solicite al usuario 5 números enteros
# (se debe validar que sean números enteros, positivos o negativos). Luego muestre lo
# siguiente: el valor mínimo, el valor máximo, la suma de los números, el promedio y
# los números ordenados de mayor a menor. No se debe usar: listas, ni otra estructura similar.

# minimo = float('inf')
# maximo = float('-inf')
# suma = 0
#
# for i in range(5):
#     while True:
#         try:
#             num = int(input(f'Ingrese el número {i + 1}: '))
#             break
#         except ValueError:
#             print('Por favor, ingresar un número entero válido.')
#
#     if num < minimo:
#         minimo = num
#     if num > maximo:
#         maximo = num
#     suma += num
#
# promedio = suma / 5
#
# print(f'Valor mínimo: {minimo}\nValor máximo: {maximo}\nSuma de los números: {suma}\nPromedio de los números: {promedio}')
