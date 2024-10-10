import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self, db_name, user, password, host, port):
        self.db_name = db_name
        self.user = user
        self.password = password 
        self.host = host
        self.port = port
        self.connection = None
    
    # Method to connect to the databse
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host = self.host,
                database = self.db_name,
                user = self.user,
                password = self.password,
                port = self.port
            )
            print("Connection established!")
        except Exception as error:
            print(f"Error connecting to the database: {error}")
    
    # Method to close the connection
    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")

    # Method to insert a customer into customers table
    def insert_customer(self, customer_name, email, phone, address, loyalty_points):
        try:
            cursor = self.connection.cursor()
            query = """
            insert into customers (customer_name, email, phone, address, loyalty_points) values (%s, %s, %s, %s, %s); 
            """
            cursor.execute(query, (customer_name, email, phone, address, loyalty_points))
            self.connection.commit()
            print("Customer inserted successfully!")
            cursor.close()

        except Exception as error:
            print(f"Error inserting data: {error}")
            self.connection.rollback()

    # Method to update a customer's loyalty points
    def update_customers(self, customer_id, customer_name = None, email = None, phone = None, address = None, loyalty_points= None):
        try:
            cursor = self.connection.cursor()
            query = """
            update Customers
            set loyalty_points = %s
            where customer_id = %s;
            """
            cursor.execute(query, (loyalty_points, customer_id))
            self.connection.commit()
            print("Loyalty points updated successfully!")
            cursor.close()

        except Exception as error:
            print(f"Error updating loyalty points: {error}")
            self.connection.rollback()

    # Method to fetch all customers
    def get_all_customers(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("Select * from customers;")
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except Exception as error:
            print(f"Error fetching customers: {error}")
            return []
        
    # Method to delete a customer by ID
    def delete_customer(self, customer_id):
        try:
            cursor = self.connection.cursor()
            query = "Delete from Customers where customer_id = %s;"
            cursor.execute(query, (customer_id,))
            self.connection.commit()
            print("Customer deleted successfully!")
            cursor.close()
        except Exception as error:
            print(f"Error deleteing customer: {error}")
            self.connection.rollback()

    # Method to insert a product
    def insert_product(self, product_name, category, product_price, stock):
        try:
            cursor = self.connection.cursor()
            query = """
            insert into Products (product_name, category, product_price, stock)
            values (%s, %s, %s, %s);
            """
            cursor.execute(query, (product_name, category, product_price, stock))
            self.connection.commit()
            print("Product inserted successfully!")
            cursor.close()
        except Exception as error:
            print(f"Error inserting product: {error}")
            self.connection.rollback()



    # Update product details (You can choose to update either price, stock or both)
    def update_product(self, product_id, Product_price = None, stock = None):
        try:
            cursor = self.connection.cursor()

            updates = []
            if Product_price is not None:
                updates.append(f"product_price = {Product_price}")
            if stock is not None:
                updates.append(f"stock = {stock}")

            update_str = ", ".join(updates)
            query = f"""
            update Products 
            set {update_str}
            where product_id = %s;
            """
            cursor.execute(query, (product_id,))
            self.connection.commit()
            print("Product updated successfully!")
            cursor.close()

        except Exception as error:
            print(f"Error updating product: {error}")
            self.connection.rollback()

    # select all product
    def get_all_products(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("Select * from Products;")
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except Exception as error:
            print(f"Error in getting products: {error}")
            return []

    # Delete a product
    def delete_product(self, product_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Products WHERE product_id = %s;"
            cursor.execute(query, (product_id,))
            self.connection.commit()
            print("Product deleted successfully!")
            cursor.close()
        except Exception as error:
            print(f"Error deleting product: {error}")
            self.connection.rollback()

    ### ORDER TABLE OPERATIONS ###

    # Insert an order
    def insert_order(self, customer_id, total_amount):
        try:
            cursor = self.connection.cursor()
            query = """
            INSERT INTO Orders (customer_id, total_amount)
            VALUES (%s, %s) Returning order_id;
            """
            cursor.execute(query, (customer_id, total_amount))
            self.connection.commit()
            print("Order inserted successfully!")
            cursor.close()
        except Exception as error:
            print(f"Error inserting order: {error}")
            self.connection.rollback()

    # Update order details (total_amount or order_date)
    def update_order(self, order_id, total_amount=None, order_date=None):
        try:
            cursor = self.connection.cursor()

            updates = []
            if total_amount is not None:
                updates.append(f"total_amount = {total_amount}")
            if order_date is not None:
                updates.append(f"order_date = '{order_date}'")

            update_str = ", ".join(updates)
            query = f"""
            UPDATE Orders
            SET {update_str}
            WHERE order_id = %s;
            """
            cursor.execute(query, (order_id,))
            self.connection.commit()
            print("Order updated successfully!")
            cursor.close()
        except Exception as error:
            print(f"Error updating order: {error}")
            self.connection.rollback()

    # Select all orders
    def get_all_orders(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Orders;")
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except Exception as error:
            print(f"Error fetching orders: {error}")
            return []

    # Delete an order
    def delete_order(self, order_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Orders WHERE order_id = %s;"
            cursor.execute(query, (order_id,))
            self.connection.commit()
            print("Order deleted successfully!")
            cursor.close()
        except Exception as error:
            print(f"Error deleting order: {error}")
            self.connection.rollback()

    ### ORDERITEMS TABLE OPERATIONS ###

    # Insert an order item
    def insert_order_item(self, order_id, product_id, quantity, item_price):
        try:
            cursor = self.connection.cursor()
            query = """
            INSERT INTO OrderItems (order_id, product_id, quantity, item_price)
            VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query, (order_id, product_id, quantity, item_price))
            self.connection.commit()
            print("Order item inserted successfully!")
            cursor.close()
        except Exception as error:
            print(f"Error inserting order item: {error}")
            self.connection.rollback()

    # Update order item (quantity, item_price)
    def update_order_item(self, order_item_id, quantity=None, item_price=None):
        try:
            cursor = self.connection.cursor()

            updates = []
            if quantity is not None:
                updates.append(f"quantity = {quantity}")
            if item_price is not None:
                updates.append(f"item_price = {item_price}")

            update_str = ", ".join(updates)
            query = f"""
            UPDATE OrderItems
            SET {update_str}
            WHERE order_item_id = %s;
            """
            cursor.execute(query, (order_item_id,))
            self.connection.commit()
            print("Order item updated successfully!")
            cursor.close()
        except Exception as error:
            print(f"Error updating order item: {error}")
            self.connection.rollback()

    # Select all order items
    def get_all_order_items(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM OrderItems;")
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except Exception as error:
            print(f"Error fetching order items: {error}")
            return []

    # Delete an order item
    def delete_order_item(self, order_item_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM OrderItems WHERE order_item_id = %s;"
            cursor.execute(query, (order_item_id,))
            self.connection.commit()
            print("Order item deleted successfully!")
            cursor.close()
        except Exception as error:
            print(f"Error deleting order item: {error}")
            self.connection.rollback()

