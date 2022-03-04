
CREATE DATABASE basedatos_anime;
CREATE USER 'usuario'@'%' IDENTIFIED BY 'usuario';
GRANT ALL PRIVILEGES ON basedatos_anime.* to 'usuario'@'%';
FLUSH PRIVILEGES;
USE dasedatos_anime;

create table Anime (
titulo varchar (60) primary key,
isbn varchar (14),
estudio varchar (50),
genero enum('aventura','terror','romance','shonen'),
fecha date,
precio decimal (4,2)
);

insert into Anime values('dragon ball','9788416401925','toei animation','shonen','1986-02-26')
