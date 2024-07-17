create table users(
	id bigserial primary key,
	first_name varchar(50),
	last_name varchar(50),
	age int,
	rating numeric(5,2)
);
create table genre(
	id serial primary key,
	title varchar(100)
);

create table film(
	id serial primary key,
	title varchar(50),
	year_ int,
	genre int,
	rating numeric(5,2),
	foreign key (genre) references genre(id) on delete cascade
);


create table comment_(
	id serial primary key,
	text_ text,
	film_id int,
	user_id bigint,
	foreign key (user_id) references users(id) on delete cascade,
	foreign key (film_id) references film(id) on delete cascade
	
);
create table film_info(
	id serial primary key,
	likes int default 0,
	dislikes int default 0,
	views_ int default 0, 
	film_id int unique ,
	foreign key (film_id) references film(id) 
);

create table actor(
	id serial primary key,
	first_name varchar(50),
	last_name varchar(50),
	birth_date date,
	rating numeric(5,2)
);

create table film_actor(
	film_id int,
	actor_id int,
	foreign key (film_id) references film(id) on delete cascade,
	foreign key (actor_id) references actor(id) on delete cascade
	
);

insert into users(first_name,last_name,age,rating) values
	('Billy','Betson',25,80.5);
insert into genre(title) values
	('Fantastic');
insert into film(title,year_,genre,rating) values
	('Injustice 5',2023,3,98.9);
insert into comment_(text_,film_id,user_id) values
	('The film is good',11,3);
insert into film_info(likes,dislikes,views_,film_id) values
	(564658568,3,564658571,11);
insert into actor(first_name,last_name,birth_date,rating) values
	('Tom','Holland','2000-01-01',95.6);
insert into film_actor(film_id,actor_id) values
	(11,2);

select * from film where year_>2020;
select * from film join genre on film.genre=genre.id;
select rating from users union select rating from actor;
select film.title,film_info.likes from film join film_info on film_info.id=film.id where film_info.likes = (select max(likes) from film_info);
update film set rating = 10.0 from film_info where film_info.film_id=film.id and film_info.likes>10 ;
delete from film using film_info where film_info.film_id=film.id and film_info.dislikes >10;

