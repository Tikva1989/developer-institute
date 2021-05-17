**exercise xp**
**Exercise 1 : Items And Customers**

-- select * from item order by price ;
-- select * from item where price >= 80 order by price desc;
-- select first_name, last_name from customers order by first_name limit 3;
-- select last_name from customers order by last_name desc;

-- select * from items;
-- alter table purchases
-- add column item_id serial not null;

-- ALTER TABLE customers 
-- ADD PRIMARY KEY (customer_id);

-- ALTER TABLE purchases 
-- ADD CONSTRAINT item_id 
-- FOREIGN KEY (item_id) 
-- REFERENCES items (item_id);



-- insert into purchases (customer_id) values ('4');
-- delete from purchases where customer_id =4;
-- auto set item_id since the fields are coneccted to each other with a unique filed.

-- insert into purchases (customer_id, item_id) values  (2,2), (4,1), (5,1), (3,3), (1,3);

-- select customer_id from customers;
-- not really usefull since there is not enoght detail
-- select customers.first_name, customers.last_name, purchases.customer_id from customers inner join purchases on customers.customer_id = purchases.customer_id;
-- select items.item, purchases.customer_id = 4 from items inner join purchases on items.item_id = purchases.item_id; 
-- select items.item = 'larg desk'and items.item = 'small desk' from items inner join purchases on items.item_id = purchases.item_id;

-- insert into items (item, price) values (4,250);
-- update items set item = 'hard drive' where price = 250; 
-- insert into purchases (item_id, customer_id) values (4,(select customer_id from customers where first_name ='Scott' and last_name='Scott'));

-- select customers.first_name, customers.last_name, items.item from customers --inner join purchases on customers.customer_id = purchases.customer_id inner join items on purchases.item_id = items.item_id;

**Exercise 2 : Dvdrental Database**

-- select * from customer;
-- select first_name ||' '|| last_name as full_name from customer;
-- select distinct create_date from customer;
-- select * from customer order by first_name desc;
-- select  film_id, title, description, release_year, rental_rate from film order by  rental_rate;
-- select address, phone from address where district = 'Texas';
-- select * from film where film_id = '15' or film_id = '150';
-- select film_id, title, description, length, rental_rate from film where title= 'Family Holiday';
-- select film_id, title, description, length, rental_rate from film where title like 'Fa%';
-- select film_id, title, replacement_cost from film order by replacement_cost limit 10;
-- select film_id, title, replacement_cost from film order by replacement_cost limit 11 offset 10;
-- another selution;
-- select title from film order by replacement_cost offset 10 fetch first 10 row only;
-- SELECT customer.customer_id, first_name, last_name, amount, payment_date FROM customer
-- INNER JOIN payment 
--     ON payment.customer_id = customer.customer_id
-- ORDER BY customer_id;
-- select film.film_id, title, inventory_id from film left join inventory on film.film_id=inventory.film_id ;
-- select city.city, country.country_id, country from city full join country on city.country_id= country.country_id order by country;
--Bouns:
-- select customer.customer_id, 
-- 	first_name||' '||last_name as full_name,
-- 	payment.amount,
-- 	payment_date,
-- 	staff_id
-- 	from customer inner join payment on customer.customer_id=payment.customer_id order by staff_id;
