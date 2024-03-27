#hacer elevado sin usar **

"""
num1 = 2
num2 = 3
contador = 1
elevado = 1
while contador <= num2:
    elevado = elevado * num1
    contador = contador+ 1

print (elevado)
"""

#Programa que genere la tabla de multiplicar de un numero partiendo desde 1
#si se escribe un numero incorrecto el programa no se ejectuta
"""
numero = int(input("INGRESA EL NUMERO ENTERO POSITIVO: "))
indice = 10
contador = 1
i = 0
tabla = 0
if numero > 0:
    while contador <= indice:
     tabla = numero * contador
     contador = contador + 1
     print(tabla) 
else: 
    print("NUMERO NO VALIDO, INGRESE UN ENTERO POSITIVO")
"""
#Crear el programa anterior peo con for
"""
numero = int(input("INGRESA EL NUMERO ENTERO POSITIVO: "))
indice = 10
contador = 1
if numero > 0:
    for i in range(indice):
        tabla = numero * (i+1)
        print(tabla)
else:
    print("INGRESE UN NUMERO NATURAL")
"""

#PROGRAMA QUE RECIBA UN NUMERO NATURAL N Y REALIZE LA SERIE 1+1/2+...1/N
"""
numero = int(input("INGRESA EL NUMERO ENTERO POSITIVO: "))
serie = 0
for i in range(numero):
    serie += (1/(i+1))
    
print(serie)
"""

#PROGRAMA QUE RECIBA UN NUMERO NATURAL N Y REALIZE LA SERIE 1*1/2*...1/N
"""
numero = int(input("INGRESA EL NUMERO ENTERO POSITIVO: "))

serie = 1 

for i in range(2, numero+1):
    if i %2 == 0 : 
            serie = serie / (1/i)
            print(serie)
    else:    
            serie = serie * (1/i)
            print(serie)

print(serie)
"""

# construir un programa que categorize la cantida de numeros positivos, negativos o nulos.
"""
numero = int(input("INGRESA LA CANTIDAD DE NUMEROS: "))

positivos = 0
negativos = 0
nulos = 0

for i in range(numero):
    ingreso = int(input("ïngresa el primer numero: "))

    if ingreso > 0:
        positivos = positivos + 1

    elif ingreso < 0:
        negativos = negativos + 1


print("numeros positivos: ", positivos,"numeros negativos: ", negativos )
"""

#PROGRAMA QUE RECIBE ALTURA, PESO Y GENERO DE PERSONAS. OBTIENE PROMEDIOS DE LA POBLACION MASCULINA Y FEMENINA
""""
numero = int(input("INGRESA LA CANTIDAD DE PERSONAS: "))

estatura_hombre = 0
estatura_mujer = 0
peso_hombre = 0
peso_mujer = 0
cant_hombres = 1
cant_mujeres = 1



for i in range(numero):
    genero = input("INGRESA EL GENERO H/M: ")
    estatura = float(input("INGRESA LA ESTATURA: "))
    peso = int(input("INGRESA EL PESO: "))

    if genero.upper() == 'H':
        peso_hombre += peso
        estatura_hombre += estatura
        cant_hombres+=1
    
    elif genero.upper() == 'M':
        peso_mujer += peso
        estatura_mujer += estatura
        cant_mujeres+=1


print("PESO PROM H: ", peso_hombre/cant_hombres)
print("ESTATURA PROM H: ", estatura_hombre/cant_hombres)
print("PESO PROM M: ", peso_mujer/cant_mujeres)
print("ESTATURA PROM M: ", estatura_mujer/cant_mujeres)
"""

#PROGRAMA QUE RECIBA UN NUMERO N Y RESUELVA LA SERIE 1^1+...+N^N
"""
numero = int(input("INGRESA EL NUMERO:  "))
suma_serie = 0

for i in range(numero):

    suma_serie+= i**i
"""