# Multiplicar dos números sin usar el símbolo de multiplicación
opcion = int(input("¿Cuál ejercicio quieres entrar?\n[1]: Multiplicar sin 'x'\n"))
if opcion == 1:
    num1 = int(input("Número que quieras multiplicar: "))
    num2 = int(input("Por cual número quieres que se multiplique: "))
    result = 0
    for i in range(num2):
        result = result + num1
        # result += num1 #Otra manera de hacerlo
        
    print(f"El resultado de la multiplicación es:{result}")

# Ingresar nombre y apellido e imprimirlo al revés
if opcion == 2:
    nombre = input("Inserte su nombre: ")
    apellido = input("Inserte su apellido: ")
    print(f"{apellido} {nombre}")
    nombreReves = nombre[::-1]
    apellidoReves = apellido[::-1]
    print(f"{nombreReves} {apellidoReves}")
    #Otra manera
    concatenacion = nombre + ' ' + apellido
    print(concatenacion[::-1])

# Escribir una función que encuentre el elemento menor de una lista
if opcion == 3:
    def elementoMenor(lista, datoMenor):
        datoMenor = lista[0]
        longList = len(lista)
        for elemento in range(1, longList, 1):
            if lista[elemento] < datoMenor:
                datoMenor = lista[elemento]
        print(f"El dato menor es: {datoMenor}")
                
    datoMenor = 0
    lista = [9,2,4,1,5,3,6,8]
    elementoMenor(lista, datoMenor)
    #Otra manera
    # lista1 = [1,2,5,3,55,-24,-13]
    # menor = 'init'
        # if menor == 'init':
    # for x  in lista1:
            # menor = x
        # else:

            # menor = x if x < menor else menor

# Escribir una función que devuelva el volumen de una esfera por su radio
# [4/3 * pi * r ** 3]
if opcion == 4:
    import math
    def volumenEsfera():
        pi = math.pi
        radio = float(input("¿Cuánto vale el radio de la esfera?: "))
        resultFinal = (4/3) * pi * (radio ** 3)
        print(f"El volumen de la esfera es: {resultFinal}")
    
    volumenEsfera()


#Escribir una función que indique si el usuario es mayor de edad
if opcion == 5:
    def mayorEdad():
        edad = int(input("¿Cuál es tu edad?: "))
        if edad >= 18:
            print("Eres mayor de edad")
        else:
            print("No eres mayor de edad")
    
    mayorEdad()
    #Otra manera
    def esMayor(usuario):
        return usuario.edad > 17

    class Usuario:
        def __init__(self, edad):
            self.edad = edad

    usuario = Usuario(15)
    usuario2 = Usuario(21)

    resultado1 = esMayor(usuario)
    resultado2 = esMayor(usuario2)
    print(resultado1, resultado2)
#Escribir si una función qu indique si un número es par o impar
if opcion == 6:
    def parImpar():
        num = int(input("¿Qué número quieres saber si es par o impar?: "))
        if num % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
    parImpar()
#Escribir una función que indique cuantas vocales tiene una palabra
if opcion == 7:
    def contarVocales(aTotal, eTotal, iTotal, oTotal, uTotal, vocalTotal):
        palabra = input("Pon una palabra: ")
        for letra in palabra:
            if letra == "a" or letra == "A":
                aTotal+=1
                vocalTotal+=1

            if letra == "e" or letra == "E":
                eTotal+=1
                vocalTotal+=1

            if letra == "i" or letra == "I":
                iTotal+=1
                vocalTotal+=1

            if letra == "o" or letra == "O":
                oTotal+=1
                vocalTotal+=1
            if letra == "u" or letra == "U":
                uTotal+=1
                vocalTotal+=1
        print(f"Vocal A: {aTotal}\nVocal E: {eTotal}\nVocal I: {iTotal}\nVocal O: {oTotal}\nVocal U: {uTotal}\nTotal Vocales: {vocalTotal}")

    aTotal = 0
    eTotal = 0
    iTotal = 0
    oTotal = 0
    uTotal = 0
    vocalTotal = 0
    contarVocales(aTotal, eTotal, iTotal, oTotal, uTotal, vocalTotal)

# Escribir una aplicación que reciba una cantidad infinita de números hasta
# decir basta, luego que devuelva la suma de los números ingresados
if opcion == 8:
    lista = []
    print("Ingrese números y para salir escriba 'basta'")
    while True:
        valor = input('Ingrese valor: ')
        if valor == 'basta':
            break
        else:
            try:
                valor1 = int(valor)
                lista.append(valor1)
            except:
                print("Dato inválido")
                exit()
    resultado = 0
    for x in lista:
        resultado += x

    print(resultado) 



#Escribir una función que reciba nombre y apellido y los vaya agregando
#A un archivo
if opcion == 9:
    def agregarNombreAArchivo(nombre, apellido):
        c = open('nombreCompleto.txt', 'a')
        c.write(nombre + ' ' + apellido + '\n')
        c.close()

    agregarNombreAArchivo('Chanchito','Feliz')