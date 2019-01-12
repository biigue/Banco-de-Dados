
create schema reservaVoo;
use reservaVoo;

-- Tabelas

create table reserva(
codReserva integer not null,
passageiro varchar(20),
prazo varchar(10),
primary key (codReserva)
);


create table rvs_trecho(
dataRT varchar(10) not null ,
codReserva integer,
idAssento integer,
idTrecho integer,
primary key (dataRT)



);

create table assento(
numero integer not null,
classe varchar(20),
primary key (numero)
);

create table horario(
diaSemana char(13)  not null,
horarioPartida varchar(20),
horarioChegada varchar(20),
idTrecho integer,
primary key (diaSemana)
);

create table voo(
numero integer not null ,
primary key (numero)

);

create table trecho(
idTrecho integer not null,
numero integer,
codAeronave integer,
origem integer,
destino integer,
primary key (idTrecho)
);

create table aeroporto(
codAeroporto integer not null,
nomeAeroporto varchar(50),
codCidade integer,
primary key (codAeroporto)

);

create table cidade(
codCidade integer not null,
nomeCidade varchar(20),
paisCidade varchar(20),
primary key (codCidade)
);

create table tipoAeronave(
codAeronave integer not null,
descricaoAeronave varchar(200),
primary key (codAeronave)
);

-- relacionamento de assento com aeronave(
create table tipoaeronave_assento(
codAeronave integer,
idAssento integer,
primary key (codAeronave, idAssento)

);


insert into reserva (codReserva, passageiro, prazo) values
(1, "Thiago", "2019/02/11"),
(2, "Lucas", "2019/02/15"),
(3, "Maria", "2019/02/17"),
(4, "Luana", "2019/03/01"),
(5, "Marcos", "2019/01/17");

insert into assento (numero, classe) values
(1, "Executiva"),
(2, "Executiva"),
(3, "Economica"),
(4, "Economica"),
(5, "Executiva");

insert into tipoAeronave (codAeronave, descricaoAeronave) values
(1, "Airbus A380"),
(2, "Boeing 707"),
(3, "Boeing 747"),
(4, "Boeing 777"),
(5, "Boeing 737");

insert into cidade (codCidade, nomeCidade, paisCidade) values
(1, "Recife", "Brasil"),
(2, "Olinda", "Brasil"),
(3, "São Paulo", "Brasil"),
(4, "Rio de Janeiro", "Brasil"),
(5, "Camaragibe", "Brasil");

insert into aeroporto (codAeroporto, nomeAeroporto, codCidade) values
(1, "Aeroporto de Recife", 1),
(2, "Aeroporto de Guarulhos", 3),
(3, "Aeroporto de Congonhas", 3),
(4, "Aeroporto do Galeão", 4),
(5, "Aeroporto Santos Dumont", 4);

insert into voo (numero) values
(5425),
(4658),
(5567),
(4698),
(4585);

insert into tipoaeronave_assento (codAeronave, idAssento) values
(1, 1),
(1, 2),
(1, 5),
(2, 3),
(2, 4);

insert into trecho (idTrecho, numero, codAeronave, origem, destino) values
(1, 5425, 1, 1, 2),
(2, 4658, 2, 1, 2),
(3, 5567, 2, 2, 1),
(4, 4698, 3, 2, 4),
(5, 4585, 4, 5, 3);

insert into rvs_trecho (dataRT, codReserva, idAssento, idTrecho) values
("2019/01/01", 1, 5, 1),
("2019/01/02", 2, 1, 1),
("2019/01/03", 3, 2, 1),
("2019/01/04", 4, 3, 3),
("2019/01/05", 5, 4, 2);

insert into horario (diaSemana, horarioPartida, horarioChegada, idTrecho) values
("Segunda", "06:30", "09:30", 1),
("Quarta", "14:30", "17:30", 1),
("Sexta", "20:30", "23:30", 1),
("Terça", "07:00", "08:00", 4),
("Quinta", "19:00", "20:00", 5);


-- chave estrangeira

alter table rvs_trecho add foreign key (codReserva) references reserva (codReserva)
on delete cascade
on update cascade;

alter table rvs_trecho add foreign key (idAssento) references assento (numero)
on delete cascade
on update cascade;

alter table rvs_trecho add foreign key (idTrecho) references trecho (idTrecho)
on delete cascade
on update cascade;

alter table horario add foreign key(idTrecho) references trecho(idTrecho)
on delete cascade
on update cascade;

alter table trecho add foreign key(numero) references voo(numero)
on delete cascade
on update cascade;

alter table trecho add foreign key(codAeronave) references tipoAeronave(codAeronave)
on delete cascade
on update cascade;

alter table trecho add foreign key(origem) references aeroporto(codAeroporto)
on delete cascade
on update cascade;

alter table trecho add foreign key(destino) references aeroporto(codAeroporto)
on delete cascade
on update cascade;

alter table aeroporto add foreign key(codCidade) references cidade(codCidade)
on delete cascade
on update cascade;

alter table tipoaeronave_assento add foreign key(codAeronave) references tipoAeronave(codAeronave)
on delete cascade
on update cascade;

alter table tipoaeronave_assento add foreign key(idAssento) references assento(numero)
on delete cascade
on update cascade;






