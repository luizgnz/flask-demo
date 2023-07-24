# Importa la clase Flask
from flask import Flask

# Crea una instancia de la clase Flask
app = Flask(__name__)

# Define la ruta raíz ("/") y asocia la función hola_mundo a esa ruta
@app.route('/')
def hola_mundo():
    return '¡Hola, Mundo!'

# Verifica si este script se está ejecutando directamente
# Si es así, inicia el servidor de Flask
if __name__ == '__main__':
    app.run()
