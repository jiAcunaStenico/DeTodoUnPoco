import random

def adivina_el_numero(x):  


  print ("========================")
  print (" ¡bienvenido al juego! ")
  print ("========================")
  print ("Tenes que adivinar el numero.")

  numero_aleatorio = random.randint (1, x)

  prediccion = 0

  while prediccion != numero_aleatorio: 
 
    prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))

    if prediccion < numero_aleatorio:
        print ("Intenta otra vez. El numero es Chico.")
    elif prediccion > numero_aleatorio:
        print ("Intenta otra vez. El numero es Grande.")

  print (f"¡Adivinaste el numero! {numero_aleatorio} correctamente.")


adivina_el_numero (35)
