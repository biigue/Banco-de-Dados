
create schema reservaVoo;
use reservaVoo;

-- Tabelas

create table reserva(
-- codigoReserva pk
codReserva integer auto_increment not null,
passageiro varchar(20),
prazo date,
primary key (codReserva)
-- n sei se o prazo ta certo sendo date
);

-- dar uma olhada nos relacionamentos/chaves estrangeiras pra ver se ta certo.
-- ver se usei a on delete e on update certo ou ver outras formas de usar ele


create table rvs_trecho(
data date not null,
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
diaSemana char(13) not null,
horarioPartida varchar(20),
horarioChegada varchar(20),
idTrecho integer,
primary key (diaSemana)
);

create table voo(
numero integer not null,
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
codAeroporto integer,
nomeAeroporto varchar(20),
codCidade integer,
primary key (codAeroporto)

);

create table cidade(
codCidade integer,
nomeCidade varchar(20),
paisCidade varchar(20),
primary key (codCidade)
);

create table tipoAeronave(
codAeronave integer,
descricaoAeronave varchar(200),
primary key (codAeronave)
);

-- relacionamento de assento com aeronave(
create table tipoaeronave_assento(
codAeronave integer,
idAssento integer,
primary key (codAeronave, idAssento)

);


alter table rvs_trecho add foreign key (codReserva) references reserva (codReserva);
alter table rvs_trecho add foreign key (idAssento) references assento (numero);
alter table rvs_trecho add foreign key (idTrecho) references trecho (idTrecho);

alter table horario add foreign key(idTrecho) references trecho(idTrecho);

alter table trecho add foreign key(numero) references voo(numero);
alter table trecho add foreign key(codAeronave) references tipoAeronave(codAeronave);
alter table trecho add foreign key(origem) references aeroporto(codAeroporto);
alter table trecho add foreign key(destino) references aeroporto(codAeroporto);

alter table aeroporto add foreign key(codCidade) references cidade(codCidade);

alter table tipoaeronave_assento add foreign key(codAeronave) references tipoAeronave(codAeronave);
alter table tipoaeronave_assento add foreign key(idAssento) references assento(numero);






