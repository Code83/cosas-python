#DIGITO VERIFICADOR PARA RUT CL
#SE PUEDE USAR PARA CREAR RUT
#no es necesario mostrar los resultados de los calculos
#pero los agregué solo para conocimiento general 

from collections import deque

#Esta es la funcion para calcular el digito
def mult(rut):
    p=int()
    y=int()
    z=int(2)
    colaRut=deque()
    print("Entramos a la funcion") 
    print(f"Vamos a calcular el digito verificador para el rut {rut}")

    colaRut=rut
    
    print(f"{colaRut}")    
    for x in reversed(colaRut):
       
        if z <=7:
         y=int(x)
         m=y*z
         p=m+p
         print(f"{y} * {z} = {m}")

         z=z+1
         
        elif z>7:
         z=2
         y=int(x)
         m=y*z
         p=m+p
         print(f"{y} * {z} = {m}")

         z=z+1     
        
        print(f"Resultado total es, {p}") 
        v_dig = p//11
        print(f"{p} / 11 = {v_dig}")
        v_dig2 = v_dig * 11
        print(f"{v_dig} * 11 = {v_dig2}")
        v_dig3 = p - v_dig2
        print(f"{p} - {v_dig2} = {v_dig3}")

        v_dig4 = 11 - v_dig3
        if v_dig4 <10:
         print(f" El digito verificador es: = {v_dig4}")

        if v_dig4 == 11:
            print("El digito verificador es = 0")
        elif v_dig4 ==10:
            print("El digito verificador es = K")   

       
#Pedimos el rut 
print("########################################################")
print("### Calculo digito verificador para los rut de CHILE ###")
print("########################################################")
v_rut = input("Ingresa un rut sin digito verificador ")
mult(v_rut)



