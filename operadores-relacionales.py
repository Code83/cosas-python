def meses(v_edad):
    v_meses=v_edad*12
   # v_dias = v_meses*30
    print (f"Haz vivido {v_meses} meses en total segun tu edad")
    return (v_meses)

print("Hola, vamos a comenzar ;)")
v_nombre = input("Cual es tu nombre? ")
v_edad = int(input("Cual es tu edad? "))
v_estatura = int(input("Cual es tu estatura en centimetros? "))

print(f"Entonces, {v_nombre}")
#uso del if
if v_estatura <= 170: 
    if v_estatura <= 0:
        print("Te estatura debe ser mayor a 0")
        print(f"Eres una persona baja, {v_nombre}")
else:    
    print(f"Eres una persona alta, {v_nombre}")

if v_edad >0:
   
   if v_edad in range (1,10):
       print("Eres muy pequeño")
       meses(v_edad)
    
   if v_edad in range (11,17):
       print("Eres todo un joven")
       meses(v_edad)
   
   if v_edad in range (18,30):
       print("Eres una persona adulta") 
       meses(v_edad)
   
   if v_edad >30:
       print("Eres un adulto fome")
       meses(v_edad) 

elif v_edad <=0:
    print("No se puede calcular tu edad porque no tienes XD")    

print("Adios")
