import psycopg2

conexion = psycopg2.connect(database="postgres",user="postgres",password="admin")
cursor1 = conexion.cursor()

sql="insert into usuarios (nombre, apellidopat, apellidomat, rut) values (%s,%s,%s,%s)"
sql2="select * from usuarios where rut = %s"

nombre = input("Ingresa tu nombre: ")
apepat = input("Ingresa tu apellido paterno: ")
apemat = input("ingresa tu apellido materno: ")
rut = input("ingresa tu rut: ")

datos = (nombre,apepat,apemat,rut)
valida = (rut)

if rut == '':
    print("No ingresaste un rut")
else:
    
#cursor1.execute(sql2,valida)
 cursor1.execute(sql,datos)

conexion.commit()
conexion.close()