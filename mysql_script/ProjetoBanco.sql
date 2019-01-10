
create schema reservaVoo;
use reservaVoo;

-- Tabelas

create table reserva(
codReserva integer not null,
passageiro varchar(20),
prazo date,
primary key (codReserva)
);


create table rvs_trecho(
data date not null ,
codReserva integer,
idAssento integer,
idTrecho integer,
primary key (data)



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
nomeAeroporto varchar(20),
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






