vector = []
for i  in range(4):
    valor = input("Ingrese valor " + str(i) + " :")
    vector [i] = valor

for i in range(4):
    for j in range(3):
        if vector [j] > vector [j+1]:
            aux = vector[j]
            vector[j] = vector[j+1]
            vector[j+1] = aux

for nro in vector:
    print (nro)