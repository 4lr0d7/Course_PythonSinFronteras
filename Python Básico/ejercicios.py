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
    print("El primer valor no es un dato numerico entero, por favor vuelva a introducir otro")
    exit()

segundo = input("Ingresa segundo número: ")

try:
    segundo = int(segundo)
except:
    segundo = 'error'

if primero == 'error' or segundo == 'error':
    print('Ingresaste mal un dato, prueba de nuevo sólo con números')
else:
    print(primero + segundo)