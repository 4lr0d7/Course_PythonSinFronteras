# WHILE LOOP
i = 0

while i < 5:
    print(i)
    # i = i + 1
    i += 1 #También se puede hacer de esta manera el incremento

#WHILE: BREAK & CONTINUE
print("-----------------")

j = 0
while j < 5:
    j += 1 #Incremente en primer lugar
    # print(j)
    if j == 3:
        # break #Ayuda a detener el loop
        continue #Salta el número 3
    # j += 1
    print(j)

#FOR LOOP
usuarios = ['Chanchito Feliz', 'Felipe', 'Roberto', 'Nicolas']
# for usuario in usuarios: #Por cada usuario en la lista de usuarios, hacer lo siguiente:
#     print(usuario)

usuario = "Chanchito Feliz"
for c in usuario: #c = caracter
    print(c)

for usuario in usuarios:
     if usuario == 'Roberto':
        # break #Rompe el ciclo de For cuando encuentra el nombre de Roberto
        continue #Omite el nombre de Roberto
     print(usuario)

for x in range(6):
    print(x)

#Para i en rango (De 3 hasta 6, pero de un paso por otro paso)
for o in range (3, 6, 1):
    print(o)
else: #Se ejecuta cuando termina de iterar todos los elementos de un range / listado / etc
    print("Hemos terminado")


usuarios1 = ['Chanchito Feliz', 'Felipe', 'Roberto', 'Nicolas']
edades = [24,25,26,35]

for usuario in usuarios1:
    for edad in edades:
        print(usuario, edad)