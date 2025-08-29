#--------------------
#Ejercicio 1
#--------------------
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad=input("Ingrese su edad: " )
#Verifico que no este vacio lo que ingresa el usuario
if not edad.strip():
   print("No ingreso ningun valor.")
elif not edad.isdigit(): #si no escribe un numero   
      print("No ingreso un numero.")
 
else:
    edad=int(edad)
    if edad >= 18 and edad < 150:
        print ("Usted es Mayor de edad")
    elif edad >=0 and edad <=17:
        print ("Usted es menor de edad")
    else: print ("usted no ha ingresado una edad que no es real")
#--------------------
#Ejercicio 2
#--------------------
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
nota=input("Ingrese la nota: " )
#Verifico que no este vacio lo que ingresa el usuario
if not nota.strip():
   print("No ingreso ningun valor.")
#no puedo usar nota.isdigit() porque  el método  no recoce números con decimales. (7.5 por ejemplo),
#  porque el punto . no es un dígito.
 
else:
    try:
        nota = float(nota)   # convierte a número decimal

        if 6 <= nota < 11:
            print("Aprobado")
        elif 0 <= nota < 6:
            print("Desaprobado")
        else:
            print("Usted no ha ingresado una nota real")
    except ValueError:
        print("No ingresó un número válido.")
#--------------------
#Ejercicio 3
#--------------------
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". numero: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.
numero=input("Ingrese un numero par: " )
#Verifico que no este vacio lo que ingresa el usuario
if not numero.strip():
   print("No ingreso ningun valor.")

 
else:
    try:
        numero = float(numero)   # convierte a número decimal
        
        if numero%2==0:
            print("El numero es par")
        else:
            print("El numero es impar")
    except ValueError:
        print("No ingresó un número válido.") # por si ingresa letra u otro caracter.

#--------------------
#Ejercicio 4
#--------------------
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.


edad=input("Ingrese su edad: " )
#Verifico que no este vacio lo que ingresa el usuario
if not edad.strip():
   print("No ingreso ningun valor.")
elif not edad.isdigit(): #si no escribe un numero   
      print("No ingreso un numero.")
 
else:
    edad=int(edad)
    if edad >= 0 and edad < 12:
        print ("Pertenece a la categoria Niño/a")
    elif edad >= 12 and edad < 18:
        print ("Pertenece a la categoria Adolecente")
    elif edad >= 18 and edad < 30:
        print ("Pertenece a la caterogia Adulto/a Joven")
    elif edad >= 30 and edad < 160:
        print ("Pertenece a la caterogia Adulto/a Mayor")

    else: print ("usted no ha ingresado una edad que no es real")
#--------------------
#Ejercicio 5
#--------------------
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

password=input("ingrese una contraseña que contenga entre 8 y 14 caacteres: ")
if 8 <= len(password) <= 14:
    print("Ha ingresaso una contraseña correcta")
else: print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#--------------------
#Ejercicio 6
#--------------------
#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
#siguiente:
#from statistics import mode, median, mean
#numeros_aleatorios= [1,2,5,5,3]
#mean(mi_lista)
#En la documentación oficial se puede encontrar más información sobre este paquete:
#https://docs.python.org/es/3.8/library/statistics.html.
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#mi_lista, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatoriosde la siguiente forma:
#import random
#numeros_aleatorios= [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.


from statistics import mode, median, mean

import random
numeros_aleatorios= [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(numeros_aleatorios)
print(media)
print(mediana)
print(moda)

if media > mediana and mediana > moda:
    print("El sesgo es positivo")
elif media < mediana and mediana < moda:
    print("El sesgo es negativo")
elif media == mediana == moda:
    print("El sesgo es nulo")
else: print("No se puede determinar el sesgo")  
#--------------------
#Ejercicio 7
#--------------------
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

palfra=input("ingrese una palabra o una frase: ")

ultima_letra=palfra[-1].lower()
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    conexclamacion = f"{palfra}!"
    print(conexclamacion)
else: print(palfra)
#--------------------
#Ejercicio 8
#--------------------
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.


nombre=input("ingrese su nombre: ")
print("#######---menu de opciones---##### ")
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas")
print("3. Si quiere su nombre con la primera letra mayúscula")

opcion = int(input("Ingrese una opción (1,2,3): "))

if opcion == 1:
    print("Elegiste la opción 1")
    print(nombre.upper())
elif opcion == 2:
    print("Elegiste la opción 2")
    print(nombre.lower())
elif opcion == 3:
    print("Elegiste la opción 3")
    print(nombre.title())
else:
    print("Opción no válida")
#--------------------
#Ejercicio 9
#--------------------
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud=float(input("Ingrese la magnitud del terremoto: "))

if magnitud<3: 
    print("Muy leve, imperceptible")
elif magnitud>=3 and magnitud<4:
   print ("Leve,ligeramente perceptible")  
elif magnitud>=4 and magnitud<5:
   print("Moderado, sentido por personas, pero generalmente no causa daños") 
elif magnitud>=5 and magnitud<6:
   print("Fuerte, puede causar daños en estructuras débiles")
elif magnitud>=6 and magnitud<7:
   print("Muy Fuerte, puede causar daños significativos") 
else:
   print("Extremo, puede causar graves daños a gran escala")     
#--------------------
#Ejercicio 10
#--------------------
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

print("#######---menu de opciones---##### ")
print("ingrese en que hemisferio se encuentra: ")
print("1. Hemisferio Norte")
print("2. Hemisferio Sur")

opcion = int(input("Ingrese una opción (1 o 2): "))
if opcion==1:
    print("#######---Ingrese el numero del mes en que se encuentra ---##### ")
    print("1 para Enero")
    print("2 para Febrero")
    print("3 para Marzo")
    print("4 para Abril")
    print("5 para Mayo")
    print("6 para Junio")
    print("7 para Julio")
    print("8 para Agosto")
    print("9 para Septiembre")
    print("10 para Octubre")
    print("11 para Noviembre")
    print("12 para Diciembre")
    mes = int(input("Ingrese una opción (1,2,3..): "))
    dia = int(input("Ingrese que dia del mes es: "))
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20): 
        print("Primavera")   
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20): 
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20): 
        print("Otoño")
    else:
        print("La opcion ingresada no existe")
elif opcion==2:
    print("#######---Ingrese el numero del mes en que se encuentra ---##### ")
    print("1 para Enero")
    print("2 para Febrero")
    print("3 para Marzo")
    print("4 para Abril")
    print("5 para Mayo")
    print("6 para Junio")
    print("7 para Julio")
    print("8 para Agosto")
    print("9 para Septiembre")
    print("10 para Octubre")
    print("11 para Noviembre")
    print("12 para Diciembre")
    mes = int(input("Ingrese una opción (1,2,3..): "))
    dia = int(input("Ingrese que dia del mes es: "))
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20): 
        print("Otoño")   
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20): 
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20): 
        print("Primavera")
    else:
        print("La opcion ingresada no existe")
           
else:
        print("La opcion ingresada no existe")           