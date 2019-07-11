matriz=[]
matriz.append(range(1,4))
matriz.append(range(4,7))
matriz.append([10,11,12])
print matriz

for i in matriz:
	print i

for i in matriz:
	for j in i:
		print j