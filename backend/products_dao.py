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

if __name__ == '__main__':
    connection = get_sql_connection()
    print(inser_new_product(connection,{
        'product_name': 'cabbage',
        'uom_id': '1',
        'price_per_unit': 90
    } ))