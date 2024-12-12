import pymysql

def connect_db():
    connection = pymysql.connect(
        host="your-rds-endpoint",
        user="your-username",
        password="your-password",
        database="ecommerce_db"
    )
    return connection

def fetch_sales_data():
    connection = connect_db()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    query = "SELECT product_name, quantity_sold, revenue FROM sales_data"
    cursor.execute(query)
    result = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return result