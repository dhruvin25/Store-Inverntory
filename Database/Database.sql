create table Products(
	product_id SERIAL primary key,
	product_name varchar(255) not null,
	category varchar(100),
	product_price decimal(10,2) not null check (product_price>=0),
	stock integer not null check (stock>=0)
);

create table Customers(
	customer_id serial primary key,
	customer_name varchar(255) not null,
	email varchar (255),
	phone varchar (20),
	address Text,
	loyalty_points integer default 0
);

create table Orders(
	order_id serial primary key,
	customer_id integer Not null references Customers(customer_id),
	order_date timestamp default current_timestamp,
	total_amount decimal(10,2)
);

create table OrderItems(
	order_item_id serial primary key,
	order_id integer not null references Orders(order_id),
	product_id integer not null references Products(product_id),
	quantity integer not null check (quantity > 0),
	item_price decimal (10,2) not null
);

-- customer insert
insert into Customers (customer_name, email, phone, address) values ('John Doe','john@gmail.com','123-456-7890','123 Elm street');
select * from Customers;

-- Customer update
update Customers set email = 'john.joe@gmail.com', address = '456 oak street' where customer_id =1;

-- product insert
insert into Products(product_name, description, product_price, stock) values ('Laptop','High-end gaming laptop', 150.00, 10);
select * from Products;
-- product update
update Products set product_price = 140.00, stock = 15 where product_id = 1;

-- product delete
delete from Products where product_id =1;


-- order insert
insert into Orders (customer_id, total_amount) values (1,350.00) returning order_id;
select * from orders;
-- orderitems insert
insert into Orderitems (order_id, product_id, quantity, item_price) values (1,1,2,1500.00);
select * from Orderitems;

-- order update (total order price)
update Orders
set total_amount = (select sum(item_price * quantity) from Orderitems where order_id = 1) where order_id = 1;

-- Steps to delete customer
-- step-1 -> delete all items associated with the customer's
delete from Orderitems where order_id in (select order_id from orders where customer_id = 1);

-- step-2 -> delete all orders placed by the customer
delete from orders where customer_id =1;

-- step-3 -> delete the customer record
delete from Customers where customer_id =1;

-- Delete a Product
delete from product where product_id =1;

--  delete order
delete from orders where order_id =1;

-- Fetch orders with associated order items
select Orders.order_id, Customers.customer_name, Products.product_name, orderitems.item_price, orderitems.quantity
from orders
join Customers ON Orders.customer_id = Customers.customer_id
join Orderitems on orders.order_id = orderitems.order_id
join products on orderitems.product_id = products.product_id
where orders.order_id = 1