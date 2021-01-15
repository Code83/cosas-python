##Agenda con diccionario

agenda = {}

cantidad = int(input("Indique cantidad de contactos a agendar: "))
if cantidad > 0:
    print("##### AGENDA #####")
    
    for c in range(0,cantidad):
        nombre = input("Nombre de contacto:")
        if nombre in agenda:
            print("{} ya existe en agenda, su numero {}".format(nombre,agenda[nombre]))
        else:
            agenda[nombre]=input("Indique numero telefonico: ")
    print("\Listado de contactos")        
    for nombre, numero in agenda.items():
        print(nombre, " -->", numero)
else:
    print("La cantidad de contactos debe ser mayor a 0")        
