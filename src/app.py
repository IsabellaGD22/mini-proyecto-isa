from flask import Flask, jsonify, request

app = Flask(__name__)

data = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    data.append(item)
    return jsonify(item), 201

@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    if index < len(data):
        data[index] = request.json
        return jsonify(data[index])
    return {"error": "Item no encontrado"}, 404

@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if index < len(data):
        deleted = data.pop(index)
        return jsonify(deleted)
    return {"error": "Item no encontrado"}, 404

if __name__ == '__main__':
    app.run(debug=True)

