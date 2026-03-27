from flask import Flask, jsonify, request
# test CI
app = Flask(__name__)

# Base de datos en memoria
data = []

# ==============================
# ENDPOINTS CRUD
# ==============================

# GET - obtener todos los items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# POST - agregar un item
@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    data.append(item)
    return jsonify(item), 201

# PUT - actualizar un item por índice
@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    if index < len(data):
        data[index] = request.json
        return jsonify(data[index])
    return jsonify({"error": "Item no encontrado"}), 404

# DELETE - eliminar un item por índice
@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if index < len(data):
        deleted = data.pop(index)
        return jsonify(deleted)
    return jsonify({"error": "Item no encontrado"}), 404


# ==============================
# FUNCIONES EXTRA (TDD)
# ==============================

def suma(a, b):
    return a + b

def es_par(n):
    return n % 2 == 0


# ==============================
# MAIN
# ==============================

if __name__ == '__main__':
    app.run(debug=True)

