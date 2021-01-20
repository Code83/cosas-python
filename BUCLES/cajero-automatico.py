from random import randrange

saldo = randrange(0,5000000)

print("***** Bienvenido a cajero automatico *****")
while True:
  print("\nOperaciones disponibles")
  print("\n1. Saldo")
  print("2. Retiro")
  print("3. Desposito")
  print("0. Salir")

  opcion = int(input("Ingresa una opcion: "))  
  if opcion in range(0,3):
      if opcion == 1:
          print("Su saldo disponible es :$", saldo)
      elif opcion == 2:
          monto = int(input("Ingreso monto a retirar: "))
          if monto > saldo:
              print("Saldo insuficiente")
          else:
            saldo = saldo - monto
            print("Operacion exitosa")      
            print("Su nuevo saldo es:", saldo)
      elif opcion == 3:
          monto = int(input("Ingrese el monto a depositar:"))  
          saldo = monto + saldo
          print("Su saldo actual es:", saldo)
      else:
          print("Adios")    
          break
  else:
        print("La opcion no es valida, intente nuevamente")    