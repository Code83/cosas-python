from flask import Flask, render_template
import psycopg2


app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

@app.route('/creaUsuario', strict_slashes=False)
def hola():
    conexion = psycopg2.connect(database="postgres",user="postgres",password="admin")
    cursor1 = conexion.cursor()
    sql="insert into usuarios (nombre, apellidopat, apellidomat, rut) values ('Hola', 'a', 'todos', 'NNNNN')"
    cursor1.execute(sql)
    conexion.commit()
    conexion.close()

    return render_template("creaUsuario.html")
# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
