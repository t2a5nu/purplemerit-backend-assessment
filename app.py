from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory list (no database)
items = []

@app.route("/")
def home():
    return jsonify({"message": "Backend API is running"})

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items", methods=["POST"])
def add_item():
    data = request.json
    items.append(data)
    return jsonify({"message": "Item added successfully"}), 201

@app.route("/items/<int:index>", methods=["DELETE"])
def delete_item(index):
    if index < len(items):
        items.pop(index)
        return jsonify({"message": "Item deleted"})
    return jsonify({"error": "Invalid index"}), 400

if __name__ == "__main__":
    app.run()
