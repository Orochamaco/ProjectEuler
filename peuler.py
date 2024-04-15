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

"""
numeros = 2000000
sum, sieve = 0, [True] * numeros


for p in range(2, numeros):
        if sieve[p]:
            sum+= p
        for i in range(p * p, numeros, p):
              sieve[i] = False

print(sum)
"""

#Problema 11

import numpy as np





matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

invertida = [[row[i] for row in matrix] for i in range(3)]




grid =   """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
            49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
            81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
            52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
            22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
            24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
            32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
            67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
            24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
            21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
            78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
            16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
            86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
            19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
            04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
            88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
            04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
            20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
            20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
            01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 """ 

#RESUELTO CON COMPRENSION DE LISTAS
"""
ss = np.array([[int(x) for x in grid.split()][i:i+20] for i in range(0,400,20)]).reshape(20, 20)

right = max(np.prod(ss[row,column:column + 2]) for row in range(20) for column in range(16))
down = max(np.prod(ss[row: row + 2, column]) for row in range(16) for column in range(20))
diagonal_right = max(np.prod([ss[row + k, column + k ] for k in range(4)])for row in range(16) for column in range(16))
diagonal_left = max(np.prod([ss[row + k, column - k ] for k in range(4)])for row in range(16) for column in range(3,20))


calculo = max([right, down, diagonal_right, diagonal_left])
print(calculo)
"""
# RESUELTO CON INDICES
"""
def calculo ():
    maximo = 0 
    #right
    for row in range(20): #0
        for column in range(16): #0
            mult = 1 
            for i in range(4): #0
                mult*= ss[row] [column + i] #[0][1]
                maximo = max(mult, maximo)
    


    #down
    for row in range(16): #0
        for column in range(20): #0
            mult = 1 
            for i in range(4): #0
                mult*= ss[row + i] [column] #[0][1]
                maximo = max(mult, maximo)




    #diagonal derecha - abajo
    for row in range(16):  #2,            
        for column in range(16): #2
                    mult = 1 
                    for i in range(4): #0 , 1
                        mult*= ss[row + i] [column + i] #[0][0]
                        maximo = max(mult, maximo)
                        
                        


    #diagonal izquierda - abajo

    for row in range(19, 3, -1):         
        for column in range(16): 
            mult = 1  
            for i in range(4): 
                mult*= ss[row - i] [column + i] 
                maximo = max(mult, maximo)

    return maximo

print(calculo())
"""

#PROBLEMA 12
from math import sqrt, floor


tri = 1
limite = 0 


def triangular(n):
    result = 0
    for i in range(1, n + 1):
        result+=i
    return result


def divisores(r):
    cont = 0
    for i in range(1, floor(sqrt(r)) + 1):
        if r % i == 0:    
                cont+= 1
        
    return cont * 2



while divisores(triangular(tri)) <= 500:
    tri+=1
print(triangular(tri))
    

"""

    lista = [True] * r
    for i in range(2, r):
        if lista[i]:
            continue
        for j in range(i * i, r, i):
              lista[j] = False

"""