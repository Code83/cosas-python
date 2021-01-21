import psycopg2

conexion = psycopg2.connect(database="postgres",user="postgres",password="admin")
cursor1 = conexion.cursor()

#Instruccion para insertar
sql="insert into usuarios (nombre, apellidopat, apellidomat, rut) values (%s,%s,%s,%s)"
#instruccion para validar usuarios
sql2="select * from usuarios where rut = '%s'"
#insetruccion para borrar por rut
delete = "delete from usuarios where rut =%s"
#instruccion para crear los vehiculos
sql3="insert into autos (marca,modelo,disponible,patente) values (%s,%s,%s,%s)"

#Definimos funcion para insertar datos en BD
#Se reciben los datos a insertar en la variable datos

def inserta(datos):
    if rut == '':
        print("rut obligatorio, no se inserta registro")
    else:
        cursor1.execute(sql,datos)

 #cursor1.execute(delete,valida) línea para permitir borrar datos por rut

        conexion.commit()
        conexion.close()
        print("Ingreso de datos OK")

#funcion para eliminar usuario por rut
def eliminar(valida):
    
    cursor1.execute(delete,valida) #línea para permitir borrar datos por rut
    conexion.commit()
    conexion.close()
    print("Usuario eliminado")

def crea_auto(datos_auto):
    cursor1.execute(sql3.datos_auto)   
    print("Ingreso OK")
    conexion.commit()
    conexion.close()

menu = int(input("""***** Ingresa una opcion *****
                    1.-Ingresar usuario 
                    2.-Borrar usuario
                    3.-Ingresar Vehiculo
                    3.-Salir :"""))
#while True:
if menu == 1:
    nombre = input("Ingresa tu nombre: ")
    apepat = input("Ingresa tu apellido paterno: ")
    apemat = input("ingresa tu apellido materno: ")
    rut = input("ingresa tu rut: ")

    datos = (nombre,apepat,apemat,rut)
    inserta(datos)

elif menu == 2:
  rut = input("Ingresa el rut del usuario a eliminar: ")
  valida = rut
  eliminar(valida)

elif menu == 3:
    marca = input("Ingresa la marca del vehiculo: ")
    modelo = input("Ingresa el modelo: ")
    kms = int(input("KMS recorridos: "))
    anofab = int(input("Año de fabricacion: "))
    disponible = input("Disponible? SI/NO:")
    patente = input("Patente: ")
    
    datos_auto = (marca,modelo,disponible,patente)
    crea_auto(datos_auto)
else:
    print("ADIOS")
    #break