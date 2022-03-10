from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        "name": "Bhanupratap",
        "items": [
            {
                'name': 'Laptop',
                'price': 60000
            }
        ]
    }
]


# Home page
@app.route('/')
def home_page():
    return render_template('index.html')


# HTTPS VERBS
# POST --> To receive data .
# GET --> To send data.

# POST REQuest
# Post store data at /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    # Get json basically means is to get the json data that browser is sending.
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET Request
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found.'})


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store['items'].append(new_item)
            return jsonify(stores)
    return jsonify({'message': 'store not found.'})


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify({'item': store['items']})

    return jsonify({'message': 'Store not found.'})


if __name__ == '__main__':
    app.run(debug=True)
