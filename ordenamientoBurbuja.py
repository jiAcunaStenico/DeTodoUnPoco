from operator import length_hint


def ordenamientoBurbuja( array ):
    length = len(array) - 1

#bucle de pasada
    for i in range(0, length):

#bucle de comparaaciones e intercambio
        for j in range(0, length) :
            if array [j] > array [j + 1]:
                aux= array [j]
                array [j] = array [j + 1  ]
                array [j + 1] = aux

    return array

boletos = [70, 90, 0, 80, 60, 85]
print ("Antes de ordenar")
print(boletos)
print ("Despues de ordenar")

print (ordenamientoBurbuja(boletos))