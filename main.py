import json
from database import Database
file_path = "config.json"

def load_db_config(file_path):
    try:
        with open(file_path,'r') as fp:
            config = json.load(fp)
        return config
    except Exception as error:
        print(f"Error loading database configuration: {error}")
        return None

def main():
    try:
        config = load_db_config(file_path)
        if config:
            db_name = config["db_name"]
            user = config["user"]
            password = config["password"]
            host = config["host"]
            port = config["port"]

        # create a database instance
        db = Database(db_name, user, password, host, port)       

        # connect to the database
        db.connect()

        # Inserting a new customer
        # db.insert_customer("Jane smith", "jane.smith@gmail.com", "123-999-7770", "993 Oak St","89")

        # Updating Customer
        # db.update_customers(2,loyalty_points=150)

        # Deleting Customer
        # db.delete_customer(1)


        # Fetching all customers
        # customers = db.get_all_customers()
        # for customer in customers:
        #     print(customer)
        
        # Inserting Product
        # db.insert_product("smartphone", "Electronics", 699.99, 150)
        # db.insert_product("Laptop", "Computers", 1200.50, 100)
        
        # Updating Product
        # db.update_product(2,stock=90)

        # Deleting Product
        # db.delete_product(2)

        # Fetching All Product
        # products = db.get_all_products()
        # for product in products:
        #     print(product)

        # Inserting Order
        # db.insert_order(1,350.00)
        # db.insert_order(1,53)
        
        # Updating Order
        # db.update_order(1,73.11)
        
        # Delete Order
        # db.delete_order(3)
        
        # Fetching all Order
        # orders = db.get_all_orders()
        # for order in orders:
        #     print(order)

        # Inserting Orderitem
        # db.insert_order_item(order_id=1,product_id=1,quantity=2,item_price=1699.99)
        # db.insert_order_item(order_id=1,product_id=1,quantity=9,item_price=2099.99)

        # Updating OrderItem
        # db.update_order_item(1,5)

        # Deleting orderitems
        # db.delete_order_item(1)


        # Fetching all Orderitems
        # orderitems = db.get_all_order_items()
        # for item in orderitems:
        #     print(item)
        # Close the database connection
        db.close()        


    except Exception as error:
        print(error)
    

if __name__ == '__main__':
    main()