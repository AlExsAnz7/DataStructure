#Listas

from itertools import count
from os import remove
from queue import Empty
from turtle import clear
from unicodedata import numeric
from collections import deque
from math import pi
import math

fruits = ['orange', 'apple', 'watermelon', 'lemon', 'peach']
print(fruits)

#append 
#Esta función se ejecuta de forma que agrega un item aleatorio (Elegido por el usuario) al final de la lista. 
fruits.append('kiwi')
print("-----------------")
print("-append")
print(fruits)

#extend
#Esta función se ejecuta de forma que extiende la lista agregando todos los ítems del iterable.
vegetables = ['carrot', 'avocado', 'tomato']
fruits.extend(vegetables)
print('-------------------------')
print("-extend")
print(fruits)

#insert
#Esta función inserta un ítem en la posición propuesta por el usuario en dos coordenadas diferentes (el primero la posicion del item en la lista, y siguiente el item a cambiar en la misma).
fruits.insert(3, 'banana')
print('----------------')
print("-insert")
print(fruits)

#remove
#Esta función retira el primer ítem de la lista cuyo valor sea igual a x o aquel que se haya propuesto por el usuario.
fruits.remove('carrot')
print('-----------------------')
print("-remove")
print(fruits)

#pop
#Esta función retira el ítem en la posición dada de la lista y lo retorna. 
itemdelete = fruits.pop(6)
print('-------------------------')
print("-pop")
print(itemdelete)
print(fruits)

#clear
#Esta función elimina todos los elementos en la lista. 
vegetables.clear()
print("--------------------------")
print("-clear")
print(vegetables)

#index
#Esta función Retorna el índice basado en cero del primer elemento cuyo valor sea igual a x. 
indexfruits = fruits.index('apple')
print("---------------------------")
print("-index")
print(indexfruits)

#count
#Esta función retorna el número de veces (propuestas por el usuario) en las que x aparezca en la lista. 
count = fruits.count("apple")
print("----------------------------")
print('-count')
print('count of apple: ', count)

#sort
#Esta función ordena los elementos de la lista in situ de forma ascendete o descendente (los elementos pueden ser usado para personalizar el orden de la lista). 
numberfruits = [11, 3, 7, 5, 2]
numberfruits.sort()
print("----------------------------")
print("-sort")
print(numberfruits)

#reverse
#Esta función invierte los elementos de la lista in situ.
fruits.reverse()
print("-------------------------------")
print("-reverse")
print(fruits) 

#copy
#Esta función retorna una copia superficial y exacta de la lista. 
copyfruits = fruits.copy()
print("-------------------------------")
print("-copy")
print(fruits)
print("copied list: ", copyfruits)
print("-------------------------------")

#Ejemplos funcionales
#1- Usando listas cómo pilas
#Usar una lista cómo pila dónde el último elemento añadido es el primer elemento retirado. 

numberstry = [1, 2, 3, 4, 5]
numberstry.append(6)
numberstry.append(7)
print('.functionalex1')
print(numberstry)
print('--------------')
numberstry.pop()
print(numberstry)
print('---------------')
numberstry.pop()
numberstry.pop()
print(numberstry)
print('---------------')

#2-Usando listas como colas
#Usar una lista cómo cola dónde el primer elemento añadido es el primer elemento retirado.

queue_fruits = deque(['apple', 'orange', 'watermelon'])
queue_fruits.append('banana')
queue_fruits.append('kiwi')
print('.functionalex2')
print(queue_fruits)
queue_fruits.popleft()
queue_fruits.popleft()
print(queue_fruits)
print('---------------')


#3-Comprensión de listas
#Estas listas son usadas para crear un segmento de la secuencia de ciertos elementos para satisfacer una condición determinada. 

fruits_squares = []
for x in range(10): 
    fruits_squares.append(x**2)
print(fruits_squares)

#Nota: Una lista de comprensión se crea a base de corchetes rodeando una expresión seguida de la declaración for y luego más declaraciones cómo for o if. 
#Por ejemplo: 

fruits_comb = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]: 
        if x != y: 
            fruits_comb.append((x, y))
print('---------------')
print(fruits_comb)

#Nota2: Las compresiones de listas pueden contener expresiones complejas y funciones anidadas: 
fruits_math = [str(round(pi, i)) for i in range(1, 6)]
print('---------------')
print(fruits_math)

#3-Listas por comprension anidadas
#Estas listas pueden ser de cualquier expresión arbitraria, incluyendo otra comprensión de listas. 

matrix = [
        [1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12],
]
print('.functionalex3')
print('---------------')
print(matrix)

fruits_matrixtrnspnd = [[row [i] for row in matrix] for i in range(4)]
print('---------------')
print(fruits_matrixtrnspnd)

#Nota: una variante de esta comprension de listas anidadas es la siguiente: 

transposed_f = []
for i in range(4): 
    transposed_f_row = []
    for row in matrix: 
        transposed_f_row.append(row[i])
        transposed_f.append(transposed_f_row)
print('---------------')
print(transposed_f)

#Nota 2: En casos reales las funciones predefinidas funcionan mejor que funciones con procedimiento complejo. La función zip() hará un buen trabajo en esos casos. 

matrix_f = list(zip(*matrix))
print('---------------')
print(matrix_f)
print('---------------')

#4-Instrucción del 
#Una forma de eliminar un ítem de una lista dado su índice en lugar de su valor es la instrucción del. Esta instrucción nes diferente del pop que al momento de eliminar el valor, directamente lo retorna.
#La instrucción del también puede utilizarse para vaciar una lista completa o secciones de la misma.

numb = [-1, 1, 66.25, 333, 333, 1234.5]
del numb[0]
print('.functiondel')
print(numb)

del numb[2:4]
print(numb)

del numb[:]
print(numb)
print('---------------')

#Nota: tambuén puede usarse para eliminar variables: 
#del numb

#5-Tuplas y secuencias
#La tupla se basa de un número de valores separados por comas: 

tupl = 12345, 54321, 'hello!'
print('.tuplesfunction')
print(tupl[0])
print(tupl)

#Nota: las tuplas pueden estar anidadas
ian = tupl, (1, 2, 3, 4, 5)
print(ian)

#Nota 2: las tuplas pueden ser inmodificables
#tupl[0] = 88888
print(tupl)

#Nota3: Sin embargo, pueden albergar elementos modificables

jsn = ([1, 2, 3], [3, 2, 1])
print(jsn)

#Contrucción de tupla vacía 

print('---------------')
tpl_empty = ()
singleton = 'hello', #<---- la coma se alberga en el elemento 
print(len(tpl_empty))
print(len(singleton))
print(singleton)
print('---------------')

#6-Conjuntos 
#Un conjunto es una coleccion no ordenada y sin elementos que se repitan. 

camera = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('.functionset')
print(camera)       #muestra que los elementos repetidos se han eliminados

print('orange' in camera)  #demuestra que los elementos existen en la tupla de forma rápida. 
print('ball' in camera)  
print('---------------')

#Muestra las letras únicas de cada palabra dentro de un conjuto

m = set('fantasy')
s = set('ilution')
print(m)        #letras unicas en m 
print(m - s)    #letras unicas en m pero no en s 
print(m | s)    #letras unicas en m o s o ambos
print(m & s)    #letras unicas en ambas letras: m y s
print(m ^ s)    #letras unicas en m o s pero no en ambas
print('---------------')

#Nota: en este tipo de dato tambien puede utilizarse la comprensión de conjuntos: 

m = {x for x in 'fantasy' if x not in 'abc'}
print(m)
print('---------------')

#7-Diccionarios
#Otro tipo de dato útil utilizado con frecuencia en Python es el Diccionario.
#El diccionario es un conjunto de pares clave:valor donde las claves deben de ser unicas.

dic = {'effect': 7688, 'cat': 8696}
dic['candy'] = 3365
print('.dictionary')
print(dic)
print(dic['effect'])
print('---------------')

del dic['cat']
dic['mouse'] = 6584
print(dic)
print('---------------')
print(list(dic))        #posiciona los elementos en forma de lista
print(sorted(dic))      #intercala los elementos dentro de la lista
print('---------------')
print('candy' in dic)
print('effect' not in dic) 
print('---------------')

#Nota: el constructor dict() crea un diccionario directamente desde secuencias de pares clave-valor. 

print(dict([('bird', 63756), ('shiny', 2467), ('coat', 5437)]))
print('---------------')

#Nota2: también se puede usar para crear diccionarios desde expresiones arbitrarias

print({x: x**2 for x in (2, 4, 6)})
print('---------------')

#Nota3: se puede utilizar para especificar los pares usando argumentos por palabra clave al ser cadenas simples.

print(dict(solar=5364, lunar=2537, ocular=8742))
print('---------------')

#8-Iteración y sus tipos
#Al iterar se puede obetner al mismo tiempo la clave y su valñor correspondiente gracias al metodo items().

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print('.iteration')
    print(k, v)
print('---------------')

#Al iterar sobre una secuencia, se puede obtener el indice de la posicion de dicho elemento junto a su valor utilizando la funcion enumerate().

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
print('---------------')

#Para poder iterar sobre una o mas secuencias al mismo tiempo, los elementos pueden agruparse con la funcion zip().

questions = ['name', 'quest', 'favorite color']
answers = [' Alex', ' the holy grail', ' pruple']

for q, a in zip(questions, answers):
    print('what is your{0}? It is{1}.'.format(q, a))
print('---------------')

#Para poder iterar sobre una secuencia en orden inverso, se especifica el orden inicial y luego se llama a la funcion reversed().

for i in reversed(range(3, 74, 5)): 
    print(i)
print('---------------')

#En caso totalmente contrario, para iterar dentro de una secuencia ordenada, se utiliza la función sorted(). Esta funcion retorna una nueva lista de forma ordenada dejando la original totalmente intacta. 

planets = ['saturn', 'mars', 'earth', 'pluto', 'venus']
for i in sorted(planets): 
    print(i)
print('---------------')

#El uso de la funcion set() en una secuencia elimina los elementos que se vean de forma duplicada. El uso de la funcion sorted() y set() sobre una secuencia es una forma de recorrer los elementos unicos de la secuencia de forma ordenada. 

planets = ['saturn', 'mars', 'earth', 'pluto', 'venus', 'mars', 'earth', 'pluto', 'moon']
for p in sorted(set(planets)): 
    print(p)
print('---------------')

#Nota: En ocasiones, se intenta cambiar una lista existente mientras se itera, sin embargo, es más sencillo y seguro crear una lista nueva dependiendo de la iteracion necesaria que se requiera. 

planets_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 49.8]
filtered_data = []
for value in planets_data:
    if not math.isnan(value): 
        filtered_data.append(value)

print(filtered_data)
print('---------------')

#9-Más acerca de condiciones
#Es posible asignar un resultado de una comparacion u otra expresion booleana a una variable gracias a las antes mencionadas comparaciones. 

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
not_null = string1 or string2 or string3
print(not_null)

#10-Comparando secuencias y otros tipos.
#Las secuencias pueden compararse con otros elementos del mismo tipo de secuencia. En este ambito se usa un orden lexicográfico. El orden lexicográfico de los strings utiliza el punto de código Unicode para poder ordenar los caracteres individualemente. 

#Ejemplos de comparación de secuencias del mismo tipo: 
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Alex' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
