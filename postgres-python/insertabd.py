import psycopg2

conexion = psycopg2.connect(database="postgres",user="postgres",password="admin")
cursor1 = conexion.cursor()
sql="insert into usuarios (nombre, apellidopat, apellidomat, rut) values (%s,%s,%s,%s)"

def inserta(req,nombre):
    cursor1.execute(sql,nombre)
    conexion.commit()
    conexion.close()
    print("Ingreso de datos OK")
