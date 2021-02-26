from mechanize import Browser

print("Enviando formulario...")
# Crear navegador.
browser = Browser()
# Abrir URL.
browser.open("http://localhost:8000/index.py")
# Seleccionar el formulario.
form = browser.select_form("contact")
# Rellenar los campos.
browser["name"] = "Recursos Python"
browser["email"] = "contacto@recursospython.com"
browser["message"] = "Hola mundo"
# Enviar.
response = browser.submit()
# Imprimir respuesta.
print(response.read())
print("Enviado.")