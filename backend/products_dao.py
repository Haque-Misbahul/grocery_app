import mysql.connector


def get_all_products():
    cnx = mysql.connector.connect(user='root', password='macbook#94',
                                host='127.0.0.1',
                                database='grocery_store')

    cursor = cnx.cursor()

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

    cnx.close()
    return response

if __name__ == '__main__':
    print(get_all_products())