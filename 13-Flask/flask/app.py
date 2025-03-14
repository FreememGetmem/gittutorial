from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial Data in my to do list
items = [
    { "id":1, "name": "Item 1", "description": "This is item 1" },
    { "id":2, "name": "Item 2", "description": "This is item 2" }
]

@app.route('/')
def home():
    return "Welcome to the sample To Do List App"

## Get: Retrieve all the items in the list

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

## get: Retrieve a specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}),400
    return jsonify(item)

## Post: Add a new item to the list
@app.route('/additems', methods=['POST'])
def add_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "The new item needs to have a name"}),400
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)
    
## Put: Update an existing item in the list
@app.route('/edititems/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}),400
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

## Delete: Remove an item from the list
@app.route('/removeitems/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = [item for item in items if item['id'] != item_id ]
    return jsonify({"result": "Item deleted"})


if __name__ == '__main__':
    app.run(debug=True)