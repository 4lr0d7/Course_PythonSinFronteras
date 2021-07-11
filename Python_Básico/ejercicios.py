#INPUT Y JUEGO DE ADIVINAR SI ESTÁ UN DATO EN LA LISTA
dato = input('Ingrese dato: ')
lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

if lista.count(dato) > 0:
    print('El dato existe: ', dato)
else:
    print('El dato no existe: ', dato)

#CALCULADORA QUE SUMA
#el int ayuda a transformar el string que el usuario inserta
primero = input("Inserte el primer número: ")

try:
    primero = int(primero)
except:
    primero = 'error'

if primero == 'error':
    print("El valor no es un dato numerico entero, por favor vuelva a introducir otro")
    exit()

segundo = input("Ingresa segundo número: ")

try:
    segundo = int(segundo)
except:
    segundo = 'error'

if segundo == 'error':
    print("El valor no es un dato numerico entero, por favor vuelva a introducir otro")
    exit()

simbolo = input("Ingrese operación a desear: ")

if simbolo == "+":
    print(f"La suma de los dos datos {primero} + {segundo} es: ", primero + segundo)
elif simbolo == "-":
    print(f"La resta de los dos datos {primero} - {segundo} es: ", primero - segundo)
elif simbolo == "/":
    print(f"La división de los datos {primero} / {segundo} es: ", primero / segundo)
elif simbolo == "^":
    print(f"La potencia de los datos {primero} ^ {segundo} es: ", primero ** segundo)
elif simbolo == "*":
    print(f"La multiplicación de los datos {primero} * {segundo} es: ", primero * segundo)
else:
    print("Elija uno de los siguientes símbolos: +, -, *, ^. Porque el que eligió no es valido.")