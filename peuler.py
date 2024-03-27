#PROBLEMA 1
"""
sumador = 0
numero = 10

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sumador+=i

print(sumador)
"""
#PROBLEMA 2
"""
suma = 0
a = 1
b = 2
suma = a + b # s = 1 + 2 # s = 2 + 3 # s = 3 + 5
a = b # a = 2           # a = 3        # a = 5
b = suma #b = 3         # b = 5        # b = 8
"""
"""
a = 0
b = 1
suma = 0
par = 0

while suma < 4000000:    
    suma = a + b
    if suma > 4000000:
        break 
    a = b
    b = suma
    print(suma)
    if suma % 2 == 0:
        par+=suma


print(par)
"""
#PROBLEMA 3 
"""
numero = 600851475143  
mayor = 0

for i in range(2, numero):
    if (numero % i == 0):
        numero = numero / i
       # print("factor: ", i)
       # print(numero)
    
print("factor", i)
"""

#PROBLEMA 4

"""
palindromo = 0
resto = 0
inverso = 0
i = 1
numero = 1
mayor = 0

def inverse(n): 
    palindromo = 0

    while n!= 0:
        resto = n % 10
        palindromo = palindromo * 10 + resto
        n = n // 10
        
    return palindromo


while numero <= 999: 

    if( i > 999 ):
       numero = numero + 1 
       i = 1

    else:    
        mult = numero * i
        i  = i + 1

        if (mult > mayor and mult == inverse(mult)):
            mayor = mult

print (mayor)
"""

#PROBLEMA 5
"""
numero  = 20
divisor = 0
indicador = 0


while True:
    for i in range(11,21):
        if numero % i == 0:
            indicador = indicador + 1
        else:
            break


    if indicador == 10:
        print(numero)
        break
    else:  
        numero = numero + 20
        indicador = 0
"""

#PROBLEMA 6
"""
square = 0
series = 0

for i in range(1, 101):
    square = square + (i ** 2)
    series = series + i

final = (series ** 2) - square
print(final)
"""

#PROBLEMA 7

"""
primo = 2
numero = 4
controlador = 0
guardar = 0
numero_primo_final = None  # Inicializamos una variable para almacenar el número primo en la posición 11

while primo < 12: 
    for i in range(1, numero + 1):
        guardar = numero % i
        if (guardar == 0 and i != 1 and numero != i):
            controlador = controlador + 1

    if controlador == 0:
        primo = primo + 1
        if primo == 12:
            numero_primo_final = numero  # Almacenamos el número primo en la posición 11

    numero = numero + 1
    controlador = 0  # Reiniciamos controlador

# Ahora puedes consultar numero_primo_11 fuera del bucle
if numero_primo_final is not None:
    print(f"El número primo en la posición 11 es: {numero_primo_final}")
else:
    print("No se encontró el número primo en la posición 11.")
"""
"""
limite = 150000
primos = list(range(2,limite + 1))
marca = [True] * len(primos)
inicio = 2
copia = []

for i, n in enumerate(primos):
    if marca[i]:
        for j in range(i + n ,len(primos), n):
            marca[j] = False

for i, v in enumerate(marca):
    if v:
        copia.append(primos[i])   

print(copia[10000])
"""

#PROBLEMA 8 
"""
numero = "73167176531330624919225119674426574742355349194934" \
         "96983520312774506326239578318016984801869478851843" \
         "85861560789112949495459501737958331952853208805511" \
         "12540698747158523863050715693290963295227443043557" \
         "66896648950445244523161731856403098711121722383113" \
         "62229893423380308135336276614282806444486645238749" \
         "30358907296290491560440772390713810515859307960866" \
         "70172427121883998797908792274921901699720888093776" \
         "65727333001053367881220235421809751254540594752243" \
         "52584907711670556013604839586446706324415722155397" \
         "53697817977846174064955149290862569321978468622482" \
         "83972241375657056057490261407972968652414535100474" \
         "82166370484403199890008895243450658541227588666881" \
         "16427171479924442928230863465674813919123162824586" \
         "17866458359124566529476545682848912883142607690042" \
         "24219022671055626321111109370544217506941658960408" \
         "07198403850962455444362981230987879927244284909188" \
         "84580156166097919133875499200524063689912560717606" \
         "05886116467109405077541002256983155200055935729725" \
         "71636269561882670428252483600823257530420752963450"

num = ("73167176531330624919225119674426574742355349194934" 
         "96983520312774506326239578318016984801869478851843" 
         "85861560789112949495459501737958331952853208805511" 
         "12540698747158523863050715693290963295227443043557" 
         "66896648950445244523161731856403098711121722383113" 
         "62229893423380308135336276614282806444486645238749"
         "30358907296290491560440772390713810515859307960866" 
         "70172427121883998797908792274921901699720888093776" 
         "65727333001053367881220235421809751254540594752243" 
         "52584907711670556013604839586446706324415722155397" 
         "53697817977846174064955149290862569321978468622482"
         "83972241375657056057490261407972968652414535100474" 
         "82166370484403199890008895243450658541227588666881" 
         "16427171479924442928230863465674813919123162824586" 
         "17866458359124566529476545682848912883142607690042" 
         "24219022671055626321111109370544217506941658960408" 
         "07198403850962455444362981230987879927244284909188" 
         "84580156166097919133875499200524063689912560717606" 
         "05886116467109405077541002256983155200055935729725" 
         "71636269561882670428252483600823257530420752963450")

import numpy as np

lista_digitos = [int(digito) for digito in numero]
lista_copia = []
digit = 0
mult = 1
low_index = 0
high_index = 13


while high_index < 1000:
    mult = 1
    subcadena = lista_digitos[low_index:high_index]

    for v in subcadena:
        mult *= v
        lista_copia.append(mult)

    low_index += 1
    high_index += 1

print(max(lista_copia))
"""

#PROBLEMA 9
"""
from math import sqrt

maximo = 1000
lista = list(range(1,101))


for i in lista:
    for j in lista:
            if j > i:
                a = (pow(j,2) - pow(i,2))
                b = 2 * j * i
                c = (pow(j,2) + pow(i,2))
                if (a**2 + b**2 == c**2):
                    if(a + b + c == 1000):
                        print(a,b,c)
                        print(a*b*c)
"""

#final = sqrt(a) * sqrt(b) * sqrt(c)
#print(final)
#if (a + b + c == 1000) and (c == a + b) and all(sqrt(x) == int(sqrt(x)) for x in [a, b, c]):
                    
#a = (pow(j,2) - pow(i,2))
#b = 2 * j * i
#c = (pow(j,2) + pow(i,2))

#PROBLEMA 10
lista_p = ()
suma = 0
primo = 2
numero = 100

for p in range(2, primo):
    for i in range(2,100):
        primo = primo % i
        if(primo == 0 and primo != i and i != 1):
            continue
        else:
            print('XD')