from flask import Flask, request, jsonify
from flask_cors import CORS
import products_dao
from sql_connection import get_sql_connection
import uom_dao
import json
import orders_dao

app = Flask(__name__)
CORS(app)

connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_products():
    try:
        products = products_dao.get_all_products(connection)
        response = jsonify(products)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error in /getProducts:", e)
        return jsonify({'error': str(e)}), 500

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    try:
        request_payload = json.loads(request.form['data'])
        product_id = products_dao.insert_new_product(connection, request_payload)
        response = jsonify({
            'product_id': product_id
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error in /insertProduct:", e)
        return jsonify({'error': str(e)}), 500

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    try:
        # Parse the request payload
        request_payload = json.loads(request.form['data'])

        # Insert the order and handle duplicates (use the modified function)
        order_id = orders_dao.insert_order(connection, request_payload)

        # Prepare the response
        response = jsonify({
            'order_id': order_id
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    except Exception as e:
        print("Error in /insertOrder:", e)
        return jsonify({'error': str(e)}), 500


@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    try:
        response = orders_dao.get_all_orders(connection)
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error in /getAllOrders:", e)
        return jsonify({'error': str(e)}), 500

@app.route('/getUOM', methods=['GET'])
def get_uom():
    try:
        response = uom_dao.get_uoms(connection)
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error in /getUOM:", e)
        return jsonify({'error': str(e)}), 500

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    try:
        return_id = products_dao.delete_product(connection, request.form['product_id'])
        response = jsonify({
            'product_id': return_id
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error in /deleteProduct:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask server for grocery app")
    app.run(port=5000)
