if 2 < 5:
    print("2 es menor que 5")

# a == b
# a < b
# a > b
# a != b
# a <= b
# a >= b
if 2 == 2:
    print("2 es igual a 2")

if 2 == 3:
    print ("2 es igual a 3")

if 2 > 5:
    print("2 es mayor a 5")

if 5 > 2:
    print("5 es mayor a 2")

if 2 != 2:
    print("2 es distinto a 2")

if 3 != 2:
    print("3 es distinto a 2")
    
if 3 >= 2:
    print("3 es mayor o igual a 2")

if 3 <= 3:
    print("3 es menor o igual a 3")

#IF, ELIF Y ELSE
#se pueden hacer if, elif y else anidados
if 2 > 5:
    print('lala')
elif 2 > 5:
    print('2 menor a 5 en el elif')
elif 2 < 5:
    print('2 menor a 5 en el elif')
else: 
    print("yo me imprimo sólo si todo lo anterior se evalua en falso")


if 2 > 5:
    print('dos es menor a 5 en if')
else:
    print('yo me imprimo sólo si todo lo anterior se evalúa en falso 2.0')

#IF CORTOS Y TERNARIOS
#If corto
if 2 > 5: print("If de una línea de código")
#Operador ternario
print('cuando devuelve true') if 5 > 2 else print("cuando devuelve falso")

if 2 < 5 and 3 > 2:
    print("Ambas devuelven true")

if 2 < 5 and 3 < 2:
    print("Hay una falsa, esto no se mostrará")

if 1 < 0 or 1 > 0:
    print("Uno de las 2 condiciones devolvió true")

if 1 > 0 or 1 < 0: #Si una condición evalúa en true, se ejecuta la instrucción
    print("Uno de las 2 condiciones devolvió true")

if 1 < 0 or 1 == 0: #Si ambas condiciones son falsasa entonces no se ejecuta
    print("No se mostrará ningún mensaje porque ambas son falses")

