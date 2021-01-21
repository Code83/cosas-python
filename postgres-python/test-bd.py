import psycopg2

conexion = psycopg2.connect(database="postgres",user="postgres",password="admin")
cursor1 = conexion.cursor()

sql="insert into usuarios (nombre, apellidopat, apellidomat, rut) values (%s,%s,%s,%s)"
sql2="select * from usuarios where rut = '%s'"
delete = "delete from usuarios where rut = %s"

menu = int(input("Ingresa una opcion 1.-Ingresar datos 2.-Borrar datos: "))

if menu == 1:
    nombre = input("Ingresa tu nombre: ")
    apepat = input("Ingresa tu apellido paterno: ")
    apemat = input("ingresa tu apellido materno: ")
    rut = input("ingresa tu rut: ")

    datos = (nombre,apepat,apemat,rut)
    
    if rut == '':
        print("rut obligatorio, no se inserta registro")
    else:
        cursor1.execute(sql,datos)

 #cursor1.execute(delete,valida) línea para permitir borrar datos por rut

        conexion.commit()
        conexion.close()
        print("Ingreso de datos OK")
else:
  rut = input("Ingresa el rut del usuario a eliminar: ")
  valida = rut
  cursor1.execute(delete,valida) #línea para permitir borrar datos por rut
  
  conexion.commit()
  conexion.close()
  print("Usuario eliminado")
