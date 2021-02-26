from cgi import FieldStorage

print("Content-Type: text/plain")
print("")
form = FieldStorage()
name, email, message = (form["name"].value, form["email"].value,
                        form["message"].value)
print("""Formulario enviado.
Nombre: %s.
Email: %s.
Mensaje: %s.
""" % (name, email, message)
)