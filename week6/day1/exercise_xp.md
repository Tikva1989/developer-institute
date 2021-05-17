-- create table item(
-- 	item_id serial,
-- 	item varchar(20) not null,
-- 	price money  not null);

-- create table customers(
-- 	customer_id serial,
-- 	first_name varchar (20) not null,
-- 	last_name varchar(30) not null
-- 	);

-- insert into item  (item, price) values ('small desk', 100), ('large desk', 300), ('fan', 80);
-- insert into customers (first_name, last_name) values ('Greg', 'Jones'), ('Sandra', 'Jones'),('Scott', 'Scott'),
-- 	('Trevor', 'Green'),('Melanie', 'Johnson');

-- select * from customers ;
-- select * from item;

-- alter table item
-- ALTER COLUMN price TYPE smallint USING price::numeric;

-- select item from item where price > 80;
-- select * from item where price >= 300; 
-- select * from customers where first_name = 'smith';
-- select * from customers where last_name = 'Jones';
-- select * from customers where first_name != 'Scott';