#import random
from random import randint
#import random as rn

##funcion para crear una lista con un tamanio dinamico
def crear_lista(tam):
	lista = []
	
	while len(lista) < tam:
		numero = randint(0,9)
		
		if not numero in lista:
			lista.append(numero)
		
	return lista

def sumar_list(lista):
	acum = 0
	
	for i in lista:
		acum += i
	
	return acum

def ordernar(lista):
	for i in range(len(lista)):
		for j in range(i+1, len(lista)):
			if lista[i] > lista[j]:
				temp = lista[i]
				lista[i] = lista[j]
				lista[j] = temp

	return lista

def ordernar2(lista):
	for i in range(len(lista)):
		for j in range(i+1, len(lista)):
			if lista[i] > lista[j]:
				lista[i], lista[j] = lista[j], lista[i]

	return lista

def suma_recursiva(lista):
	if lista == []:
		return 0
	
	return lista[0] + suma_recursiva(lista[1:]) ##haga una suma recursiva siempre desde el item 1 hasta el final

def fibonacci(n):
	if n in [1,2]:
		return 1
	else
	
lista = crear_lista(5)
print lista
print sumar_list(lista), suma_recursiva(lista)
print ordernar2(lista)

"""
for i in range(5):
	a=raw_input("Prueba tu suerte, ingresa un valor de no mas de tres caracteres: ")
	
	if len(a) <> 3:
		print "La longitud maxima de la cadena es de tres digitos"
		break
		
	indice = 0
	picas = 0
	fijas = 0

	for lt in range(len(a)):
		if lista[lt]==int(a[lt]):
			fijas += 1
		elif int(a[lt]) in lista:
			picas += 1
	#for letra in a:
	#	if lista[indice]==int(letra):
	#		fijas += 1
	#	elif int(letra) in lista:
	#		picas += 1
	#       indice += 1

	##while indice < len(a):
                #if lista[indice]==int(a[indice]):
		#	fijas += 1
		#elif int(a[indice]) in lista:
		#	picas += 1
		
	
	if fijas == len(a):
		print "Felicidades, has obtenido todas las fijas"
		break
	else:
		print "Obtuviste " + str(fijas) + " fijas y " + str(picas) + " picas"
		
"""