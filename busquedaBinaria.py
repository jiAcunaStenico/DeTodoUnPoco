lista = [0, 88, 72, 21, 14, 16, 90, 35, 47, 6, 68, 12, 10, 54, 41]
#print(lista)
#funcion de prdenamiento de python
lista.sort() 
#print(lista)


 def busquedaBinaria(valor):
    
    inicio = 0  
    
    fin = len(lista) - 1
    
    while inicio <= fin :
        puntero = (inicio + fin) //2
        if valor == lista[puntero]:
            return puntero

        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1
    return None



 def buscar_valor(valor):
    res_busqueda = busquedaBinaria(valor)
    if res_busqueda is None:
        return f"El numero {valor} no se encontro"
    else:
        return f"El numero {valor} se encuentra en la posicion {res_busqueda}"
   

print (buscar_valor(72)) 