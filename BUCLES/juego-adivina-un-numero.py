#Importar libreria random, la función randint

from random import randint

x = randint(1,25)

intentos = 0

while intentos <=6:
    numero = int(input("Elije un numero entre 1 y 25: "))
    intentos = intentos + 1
    if numero > x:
        print("Tu numero es menor a 25")
    elif numero < x:
        print("Tu numero es mayor10 a 1")
    else:
        break
if numero == x:
    print("Bien!!! eres un adivino")
    print("Lo lograste en {} intentos".format(intentos))
else:
        print("Perdiste :( ")
        
