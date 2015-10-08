-- init database

drop database if exists awesome;

create database awesome;

use awesome;

grant select, insert, delete on awesome.* to 'www-data'@'localhost' identified by 'www-data';

create table users(
	`id` varchar(50) not null,
	`email` varchar(50) not null,
	`password` varchar(50) not null,
	`admin` bool not null,
	`name` varchar(50) not null,
	`image` varchar(500) not null,
	`created_at` real not null,
	unique key `idx_email` (`email`),
	key `idx_created_at` (`created_at`),
	primary key (`id`)
)engine=innodb default charset=utf8;

create table blogs(
	`id` varchar(50) not null,
	`user_id` varchar(50) not null,
	`user_name` varchar(50) not null,
	`user_image` varchar(500) not null,
	`name` varchar(50) not null,
	`summary` varchar(200) not null,
	`content` mediumtext not null,
	`created_at` real not null,
	key `idx_created_at` (`created_at`),
	primary key (`id`) 
)engine=innodb default charset=utf8;

create table comments(
	`id` varchar(50) not null,
	`blog_id` varchar(50) not null,
	`user_id` varchar(50) not null,
	`user_name` varchar(50) not null,
	`user_image` varchar(500) not null,
	`content` mediumtext not null,
	`created_at` real not null,
	key `idx_created_at` (`created_at`),
	primary key (`id`)
)engine=innodb default charset=utf8;

-- email / password
-- admin@example.com / password

insert into users(`id`, `email`, `password`, `admin`, `name`, `created_at`) values ('0014442895491183b4dcfc2068e45b39a5e2b5a5f1a96bf000', 'admin@example.com', 'adminpwdsxl', 1, 'Administrator', 1444288507.812);