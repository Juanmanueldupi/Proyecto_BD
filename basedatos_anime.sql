

CREATE DATABASE basedatos_anime;
CREATE USER 'usuario'@'%' IDENTIFIED BY 'usuario';
GRANT ALL PRIVILEGES ON basedatos_anime.* to 'usuario'@'%';
FLUSH PRIVILEGES;
USE basedatos_anime;

create table Anime (
titulo varchar (100) primary key,
isbn varchar (14),
estudio varchar (50),
genero enum('Supernatural','Seinen','Romance','Shonen','Action'),
fecha date,
precio decimal (4,2)
);

insert into Anime values('Dragon ball','9788416401925','Toei animation','Shonen','1986-02-26','15.90');
insert into Anime values('Boku no Herō Akademia','5467325678954','Bones','Shonen','2016-04-03','22.10');
insert into Anime values('Bungou Stray Dogs','4839026532879','Bones','Seinen','2014-05-23','25.50');
insert into Anime values('Gakusen Toshi Asterisk 2nd Season','2849462843920','A-1 Pictures','Romance','1999-07-21','14.90');
insert into Anime values('Onigiri','7894738193748','Pierrot Plus','Supernatural','1992-04-12','21.90');
insert into Anime values('Bishoujo Senshi Sailor Moon Crystal Season III','3894029485723','Toei animation','Romance','2005-09-03','10.90');
insert into Anime values('Battle Spirits: Double Drive','7867453628945','Bandai Namco Pictures','Action','2015-11-12','25.90');
