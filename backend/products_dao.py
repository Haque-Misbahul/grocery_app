from sql_connection import get_sql_connection


def get_all_products(connetion):
    

    cursor = connetion.cursor()

    query = """
        SELECT products.product_id, products.products_name, products.uom_id, uom.uom_name, products.price_per_unit
        FROM products
        INNER JOIN uom ON products.uom_id = uom.uom_id
    """
    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, uom_name, price_per_unit) in cursor:
        response.append(
            {
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
            }
        )

    return response

def inser_new_product(conncection, product):
    cursor = conncection.cursor()
    query = """ insert into 
                products (products_name, uom_id, price_per_unit)
                values (%s, %s, %s)"""

    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(conncection, product_id):
    cursor = conncection.cursor()
    query = "DELETE FROM products WHERE product_id = %s"
    cursor.execute(query, (product_id,))
    connection.commit()
    cursor.close()
    return f"Product with ID {product_id} deleted successfully."

if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 8))