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

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))