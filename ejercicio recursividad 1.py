def divisores(num):
	return [x for x in range(1, num) if num % x == 0]

def divisores_rec(num, aux):
	if aux == num:
		return []
	if num % aux == 0:
		return [aux] + divisores_rec(num, aux + 1)
	
	return divisores_rec(num, aux +1)

def suma_lista(lista):
	acum = 0
	
	for l in lista:
		acum += l
	
	return acum

def perfecto(numero):
	return sum(divisores(numero)) == numero
	
num = input("Ingrese un numero: ")
print divisores(num), divisores_rec(num, 1)

lista_div = divisores_rec(num, 1)

suma_divis = suma_lista(lista_div)

if (perfecto(num)):
	print "La suma de los divisores de " + str(num) + " es " + str(suma_divis) + " es un numero perfecto"
else:
	print "La suma de los divisores de " + str(num) + " es " + str(suma_divis) + " no es un numero perfecto"

nums = 1

lista_perfectos = []

while len(lista_perfectos) < 4:
	if perfecto(nums):
		lista_perfectos.append(nums)
	nums += 1

print lista_perfectos