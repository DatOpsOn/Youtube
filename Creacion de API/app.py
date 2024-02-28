from flask import Flask, request, jsonify
from func import *

app = Flask(__name__)

# Endpoint raíz que devuelve un mensaje de bienvenida
@app.route('/', methods=['GET'])
def welcome():
    return "Bienvenido al servidor de prueba!"

# Endpoint que acepta datos en formato JSON y devuelve una confirmación
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json  # Obtiene los datos JSON enviados en la petición
    # Aquí puedes procesar los datos según sea necesario
    return jsonify({'message': 'Datos recibidos con éxito!', 'yourData': data})

# Endpoint que devuelve el estado del servidor
@app.route('/status', methods=['GET'])
def server_status():
    return jsonify({'status': 'Activo'})


# Endpoint que acepta datos en formato JSON y devuelve una confirmación
@app.route('/suma', methods=['POST'])
def suma():
    data = request.json  # Obtiene los datos JSON enviados en la petición
    r = sum(data["a"], data["b"])
    # Aquí puedes procesar los datos según sea necesario
    return jsonify({'message': 'Datos recibidos con éxito!', 'result': r})

# Endpoint que acepta datos en formato JSON y devuelve una confirmación
@app.route('/resta', methods=['POST'])
def resta():
    data = request.json  # Obtiene los datos JSON enviados en la petición
    r = rest(data["a"], data["b"])
    # Aquí puedes procesar los datos según sea necesario
    return jsonify({'message': 'Datos recibidos con éxito!', 'result': r})

if __name__ == '__main__':
    app.run(port=6000,debug=True)  # Inicia el servidor en modo de depuración
