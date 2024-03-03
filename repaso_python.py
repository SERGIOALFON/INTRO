#cadena de textos
# print('hola mundo')
#
# print('hola python')
#
# print('estoy','aprendiendo','python')

#cadena de numeros enteros
# print(1,2,3,4)
#
# print('soy sergio', 2003)

#variable
# texto = 'hola python'
# año = 2024
# print(texto, año)

#parametro sep y end
# print(1,2,3)
# print(1,2,3, sep=',')
# print(1,2,3, sep=',', end='.')

#input
# print('introduzca su nombre')
# nombre = input()
# print('introduzca su apellido')
# apellido = input()
# print('hola', nombre, apellido)

#input más sencillo
# nombre = input('introduzca su nombre:')
# apellido = input('introduzca su apellido:')
# print('hola', nombre, apellido)

#operaciones aritmetica

#suma
# numero1 = int(input('primer sumando: '))
# numero2 = int(input('segundo sumando: '))
# print('resultado: ', numero1 + numero2)

#división entera
# dividiendo = int(input('dividiendo: '))
# divisor = int(input('divisor: '))
# print('resultado: ', dividiendo // divisor)

#división reales
# dividiendo = float(input('dividiendo: '))
# divisor = float(input('divisor: '))
# print('resultado: ', dividiendo / divisor)

#exponente
# base = int(input('base: '))
# exponente = int(input('exponente: '))
# print('resultado: ', base ** exponente)

#resta de numeros decimales float
# minuendo = float(input('minuendo: '))
# sustraendo = float(input('sustraendo: '))
# print('resultado: ', minuendo - sustraendo)

#multiplicación
# multiplicando = float(input('multiplicando: '))
# multiplicador = float(input('multiplicador: '))
# print('resultado: ', multiplicando * multiplicador)

#boleanos
# verdadero = True
# falso = False
# print('valor de la variable verdadero:', verdadero)
# print('valor de la variable falso:', falso)

#operadores logicos

#and
# print('resultado de True and True:', True and True)
# print('resultado de True and False:', True and False)
# print('resultado de False and True:', False and True)
# print('resultado de False and False:', False and False)

#or
# print('resultado de True or True:', True or True)
# print('resultado de True or False:', True or False)
# print('resultado de False or True:', False or True)
# print('resultado de False or False:', False or False)

#not
# print('resultado de not True:', not True)
# print('resultado de False:', not False)

#operadores relacionales
# numero1 = float(input('Primer número:'))
# numero2 = float(input('Segundo número:'))
# numero3 = float(input('Tercer número:'))
# numero4 = float(input('Cuarto número:'))
# print(numero1,'==',numero4,':',numero1==numero4)
# print(numero2,'!=',numero3,':',numero2!=numero3)
# print(numero3,'>',numero2,':',numero3>numero2)
# print(numero4,'<',numero1,':',numero4<numero1)
# print(numero1,'>=',numero3,':',numero1>=numero3)
# print(numero2,'<=',numero4,':',numero2<=numero4)

#cadena de texto
# cadena1 = "Hola soy Sergio Bermúdez"
# cadena2 = 'Hola soy Sergio Bermúdez'
# print(cadena1)
# print(cadena2)

#caracteres en cadena de texto
# cadena = 'SERGIO'
# print('caracter posición 0:', cadena[0])
# print('caracter posicion 1:', cadena[1])
# print('caracter posición 2:', cadena[2])
# print('caracter posición 3:', cadena[3])
# print('caracter posición 4:', cadena[4])
# print('caracter posición 5;', cadena[5])

#concatenar y multiplicar cadenas de textos
# cadena1 = input('introduzca la primera cadena:')
# cadena2 = input('introduzca la segunda cadena:')
# cadena3 = input('introduzca la tercera cadena:')
# cadenasuma = cadena1 + ' ' + cadena2 + ' ' + cadena3
# cadenamultiplicación = (cadena2 + ' ') * 5
# print('concatenada:', cadenasuma)
# print('multiplicada:', cadenamultiplicación)

#in
# cadena1 = input('introduzca la cadena1:')
# cadena2 = input('introduzca la cadena2:')
# print('¿esta la cadena2 en la cadena1?:', cadena2 in cadena1)

#funciones
#len
# cadena1 = input('introduzca la primera cadena')
# print('longitud de la cadena1 (len):', len(cadena1))

#upper
# cadena1 = input('introduzca la primera cadena')
# print('cadena1 todo mayuscula (upper):', cadena1.upper())

#lower
# cadena1 = input('introduzca la primera cadena')
# print('cadena1 todo minuscula (lower):', cadena1.lower())

#capitalize
# cadena1 = input('introduzca la primera cadena')
# print('cadena1 primera mayuscula (capitalize):', cadena1.capitalize())

#title
# cadena1 = input('introduzca la primera cadena')
# print('cadena1 primera de cada palabra mayuscula (title):', cadena1.title())

#lista con elementos
# lista = ['sergio', 'a', 39, 'ans', 'et est originaire', 'd equatour']
# print(lista)
# print(lista[0])
# print(lista[1])
# print(lista[2])
# print(lista[3])
# print(lista[4])
# print(lista[5])

#añadir elementos
# lista = ['sergio', 'alfonso', 'lupe']
# print(lista)
# lista = lista + ['johann']
# print(lista)
# lista = lista + ['chola']
# print(lista)
# lista = lista + ['kinto', 'kent']
# print(lista)

#modificar elemento de la lista y borrar un elemento
# lista = ['sergio', 'lupe', 'alfonso', 'johann', 'kinto', 'kent']
# print(lista)
# lista[2] = 'chola'
# print(lista)
# del lista[2]
# print(lista)
# lista = lista + ['johanna']
# print(lista)

#lista y sus funciones
#appned añade elemento
# lista = [45, 54, 33, 23, 12,]
# print(lista)
# lista.append(15)
# print(lista)
#sort ordena los elementos
# lista.sort()
# print(lista)
#reverse lista al reves
# lista.reverse()
# print(lista)
# lista.insert(23, 33)
# print(lista)

#truple con elementos
# tupla = ('casa', 22, 12, 'carro', 15)
# print(tupla)
# print(tupla[0])
# print(tupla[1])
# print(tupla[2])
# print(tupla[3])
# print(tupla[4])
#tupla count
# print('numero de elementos 15:', tupla.count(15))
#tupla posición de elemento
# print('posición elemento perro:', tupla.index('carro'))

#concatenar tupla
#tupla1 = (1, 2, 3, 4, 'linea')
#print(tupla1)
#tupla2 = ('puntero', 'brechero', 'comandante', 'escopetero')
#print(tupla2)
#print('numero de elementos tupla1:' , len(tupla1))
#print('numero de elementos tupla2:' , len(tupla2))
# concatenada = tupla1 + tupla2
# print('concatenada:' , concatenada)

#diccionarios
# díasdelasemanaenfrances = {'lunes' : 'lundi',
#                            'martes' : 'mardi',
#                            'miercoles' : 'mercredi',
#                            'jueves' : 'jeudi',
#                            'viernes' : 'vendredi',
#                            'sabado' : 'samedi',
#                            'domingo' : 'dimanche'}
# print(díasdelasemanaenfrances['lunes'])
# print(díasdelasemanaenfrances['miercoles'])
# print(díasdelasemanaenfrances['viernes'])
# print(díasdelasemanaenfrances['domingo'])
# print('numero de elementos del diccionario:' , len(díasdelasemanaenfrances))
# print('elemento mayor del diccionario:' , max(díasdelasemanaenfrances))
# print('elemento menor del diccionario:' , min(díasdelasemanaenfrances))


#operadores relacionales identación
# Comparación de mayor que
# a = 5
# b = 3
# if a > b:
#     print("a es mayor que b")

# Comparación de menor que
# if a < b:
#     print("a es menor que b")
# else:
#     print("a no es menor que b")

# Comparación de mayor o igual que
# c = 5
# if c >= a:
#     print("c es mayor o igual que a")

# Comparación de menor o igual que
# d = 5
# if d <= c:
#     print("d es menor o igual que c")

# Comparación de mayor que
# a = 5
# b = 3
# mayor_que = a > b
# print("a > b:", mayor_que)

# Comparación de menor que
# menor_que = a < b
# print("a < b:", menor_que)

# Comparación de mayor o igual que
#c = 5
# mayor_o_igual_que = c >= a
# print("c >= a:", mayor_o_igual_que)

# Comparación de menor o igual que
# d = 5
# menor_o_igual_que = d <= c
# print("d <= c:", menor_o_igual_que)

#uso de if, elif, else
# numero1 = int(input('escriba el primer numero: '))
# numero2 = int(input('escriba el segundo numero: '))
# if numero1==numero2:
#     print('ambos numeros son iguales')
# elif numero1>numero2:
#     print('el primer numero es mayor que el segundo')
# else:
#     print('el primer numero es menor que el segundo')

#Bucles
#FOR
#lista = ['sergio', 'patrón', 'alfonso', 'lupe']
#for item in lista:
#    print(item)
#    print(item, end=' ')

#bucle for interaciones
# for item in range(5):
#     for item2 in range(3):
#         print('interacion' + str(item) + ',' + str(item2))

#while
# i = 0
# while i<10:
#     print(i)
#     print(i, end=' ')
#     i = i + 1

#pedir numero
# pedirnumero = True
# while pedirnumero:
#     valor = int(input('introduce numero inferior a 10'))
#     if valor<10:
#         pedirnumero = False
#         print(('FIN, ha introducido un valor inferior a 10'))

#while interaciones
# item1 = 0
# while item1<5:
#     item2 = 0
#     while item2<3:
#         print('interaciones' + str(item1) + ' , ' + str(item2))
#         item2 = item2 + 1
#         item1 = item1 + 1

#interacines for y while
# for item1 in range(5):
#     item2 = 0
#     while item2<3:
#         print('interación' + str(item1) + ' , ' + str(item2))
#         item2 = item2 + 1

#función def
# def hola():
#     return '¡Hola! ¿ingresa tu password?'
# print('Primera invocación: ' + hola())
# print('Segunda invocación: ' + hola())

#funcion sumar
# Definir una función que suma dos números ingresados por el usuario
# def sumar():
#     sum1 = int(input('Sumando uno: '))
#     sum2 = int(input('Sumando dos: '))
#     print('La suma es:', sum1 + sum2)
# Llamar a la función sumar
#sumar()

#funcion restar
# def restar():
#     minuendo = int(input('minuendo: '))
#     sustraendo = int(input('sustraendo: '))
#     print('La resta es:', minuendo - sustraendo)
# Llamar a la función restar
#restar()

#funcion multiplicar
# def multiplicar():
#     multiplicando = int(input('multiplicando:'))
#     multiplicador = int(input('multiplicador:'))
#     print('la multiplicación es:', multiplicando * multiplicador)
#llamar a la funcion multiplicar
#multiplicar()

#funcion dividir
# def dividir():
#     dividiendo = int(input('dividiendo:'))
#     divisor = int(input('divisor:'))
#     print('la division es:', dividiendo / divisor)
#llamar la funcion dividir
#dividir()

#excepciones
#try
# try:
#     print(str(17/0))
# except:
#     print('error:división por 0')

#fichero lectura
# f = open('prueba.txt','r')
# texto = f.read()
# print(texto)
# f.close()

#fichero agregar escritura
# Abrir el fichero prueba.txt en modo agregar
# f = open('prueba.txt', 'a')
# Escribir una cadena de texto en el fichero
# f.write('soy de ecuador.\n')
# Escribir una lista de cadenas de texto en el fichero
# f.writelines(['soy soldado.\n', 'del ejercito.\n'])
# Cerrar el fichero
# f.close()

#programación orientada a objetos
# class Persona:
#     def __init__ (self, nombre, apellidos, edad):
#         self.Nombre = nombre
#         self.Apellidos = apellidos
#         self.Edad = edad
#     def mostrarPersona(self):
#         print('Nombre: ' + self.Nombre)
#         print('Apellidos: ' + self.Apellidos)
#         print('Edad: ' + str(self.Edad))
# p1 = Persona('Sergio Alfonso', 'Bermúdez Andrade', '39 años')
# p1.mostrarPersona()

#herencia
# Definir la clase padre Persona
#class Persona:
    # Definir el método constructor con los atributos comunes
    # def __init__(self, nombre, apellido, edad):
    #     self.nombre = nombre
    #     self.apellido = apellido
    #     self.edad = edad

    # Definir un método para mostrar los datos de la persona
    # def mostrar_datos(self):
    #     print(f"Nombre: {self.nombre}")
    #     print(f"Apellido: {self.apellido}")
    #     print(f"Edad: {self.edad}")

# Definir la clase hija Estudiante que hereda de Persona
#class Estudiante(Persona):
    # Definir el método constructor con los atributos específicos
    #def __init__(self, nombre, apellido, edad, carrera, matricula):
        # Llamar al método constructor de la clase padre
        #Persona.__init__(self, nombre, apellido, edad)
        # Asignar los atributos propios de la clase hija
        # self.carrera = carrera
        # self.matricula = matricula

    # Definir un método para mostrar los datos del estudiante
    #def mostrar_datos(self):
        # Llamar al método mostrar_datos de la clase padre
        #Persona.mostrar_datos(self)
        # Mostrar los atributos propios de la clase hija
        #print(f"Carrera: {self.carrera}")
        #print(f"Matrícula: {self.matricula}")

# Crear un objeto de la clase Estudiante
#e1 = Estudiante("Ana", "Pérez", 20, "Ingeniería", "123456")
# Llamar al método mostrar_datos del objeto
#e1.mostrar_datos()


