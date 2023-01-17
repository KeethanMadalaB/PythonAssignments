import mysql.connector

# Connecting to the MySQL database
connection = mysql.connector.connect(user='root', password='rps@123', host='localhost', database='kpmg')
cursor = connection.cursor()

# Creating the product
def creation(name, price):
    query = "INSERT INTO products (name, price) VALUES (%s, %s)"
    values = (name, price)
    cursor.execute(query, values)
    connection.commit()
    print("Product created successfully.")

# Reading all products
def reading():
    query = "SELECT * FROM products"
    cursor.execute(query)
    products = cursor.fetchall()
    for product in products:
        print(product)

# Update a product
def updation(id, name, price):
    query = "UPDATE products SET name = %s, price = %s WHERE id = %s"
    values = (name, price, id)
    cursor.execute(query, values)
    connection.commit()
    print("Product updated successfully.")

# Deleting a specific product
def delete_product(id):
    query = "DELETE FROM products WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    print("Product deleted successfully.")

# Close the database connection
def close_connection():
    cursor.close()
    connection.close()
    print("Connection closed.")
