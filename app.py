from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Product API is running."})

@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Product A"},
        {"id": 2, "name": "Product B"}
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
