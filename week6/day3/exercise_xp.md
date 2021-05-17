** Exerxise 1 **
-- select distinct name from language;
-- select film.title, description, language.name from film left join language on film.language_id=language.language_id ;
-- select film.title, description, language.name from film right join language on film.language_id=language.language_id;

-- create table new_film (
-- 	id integer primary key,
-- 	name varchar (50) not null);

-- insert into new_film (id, name) values(6000, 'Armagedon'), (7000, 'Bob Sponge');
-- select * from new_film;

-- create table customer_review(
-- review_id serial primary key not null,
-- film_id integer ,
-- language_id integer ,
-- title varchar(50) not null,
-- score smallint not null check (score >1 and score < 10),
-- review_text text,
-- last_update date,
-- constraint fk_new_film
-- foreign key (film_id) references new_film(film_id) on delete
-- );

-- CREATE TABLE customer_review(
--    review_id INT not null,
--    film_id INt ,
--    language_id int ,
--    title VARCHAR(255) NOT NULL,
--    score int check(score< 10 and score>1),
--    review_text text ,
--    last_upadete date not null ,
--    PRIMARY KEY(review_id),
--    CONSTRAINT fk_customer
--       FOREIGN KEY(film_id) 
-- 	  REFERENCES new_film(id)
-- 	  ON DELETE cascade);
-- alter table customer_review add constraint fk_language foreign key (language_id) references language(language_id);	 
	
-- select * from customer_review ;
-- insert into customer_review (review_id, film_id, language_id, title, score, review_text, last_upadete) values (1, 6000, 1, 'not recommanded', 2, 'This movie is not that good', '05\15\2021'), 
-- (2, 7000, 1, 'Graet!!', 8, 'Writen really good, reat actores, love the whole theame', '01/01/2021');
-- select * from customer_review;
-- delete from new_film where id = 6000;
-- select * from customer_review;
-- the row tath contains the film_id= 6000 deleted.

-- **Exercise 2**
-- update film set language_id = 2 where title like 'Fan%';
-- customer defined address_id as fk insert into customers not existing addres_id will raise an error.
-- drop table customer_review;
-- select count(rental_id) from rental where return_date is null;

-- select replacement_cost from film inner join inventory on film.film_id= inventory.film_id inner join rental on inventory.inventory_id= rental.inventory_id where rental.return_date is null limit 30;

--first movie:
-- select film.title from film inner join film_actor on film.film_id=film_actor.film_id inner join actor on film_actor.actor_id=actor.actor_id where description like '%sumo wrestler%' and actor.first_name= 'Penelope' and actor.last_name= 'Monroe';

-- 2nd film:
-- select film.title from film inner join film_category on film.film_id=film_category.film_id inner join category on film_category.category_id=category.category_id where category.name = 'documentary' and film.length < 60 and film.rating = 'R';


