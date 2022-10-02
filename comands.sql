CREATE DATABASE IF NOT EXISTS ABD_ORM;
USE ABD_ORM;

CREATE TABLE IF NOT EXISTS Pokemon (
    id_pok            INTEGER         PRIMARY KEY,
    nome              VARCHAR(150)    NOT NULL,
    hp                INTEGER         NOT NULL,
    atk               INTEGER         NOT NULL,
    defense           INTEGER         NOT NULL,
    special_atk       INTEGER         NOT NULL,
    special_defense   INTEGER         NOT NULL,
    speed             INTEGER         NOT NULL
);

CREATE TABLE IF NOT EXISTS Tipo (
    id_tipo    INTEGER        PRIMARY KEY,
    tipo        VARCHAR(150)   NOT NULL
);

CREATE TABLE IF NOT EXISTS Usuario (
    id_user    INTEGER         PRIMARY KEY,
    nome       VARCHAR(150)    NOT NULL,
    email      VARCHAR(150)    NOT NULL
);

CREATE TABLE IF NOT EXISTS Ranking (
    id_user    INTEGER    PRIMARY KEY,
    position   INTEGER    NOT NULL,
    vitorias   INTEGER    NOT NULL
);

CREATE TABLE IF NOT EXISTS Medalha (
    medal_id    INTEGER        PRIMARY KEY,
    id_user     INTEGER        NOT NULL,
    nome        VARCHAR(150)   NOT NULL,
    id_torneio  INTEGER        NOT NULL
);

CREATE TABLE IF NOT EXISTS Torneio (
    id_torneio    INTEGER         PRIMARY KEY,
    id_local      INTEGER         NOT NULL,
    nome          VARCHAR(150)    NOT NULL
);

CREATE TABLE IF NOT EXISTS Local_ (
    id_local    INTEGER         PRIMARY KEY,
    local_      VARCHAR(150)    NOT NULL
);

CREATE TABLE IF NOT EXISTS Pok_Tipo (
    id_pok    INTEGER    NOT NULL,
    id_tipo   INTEGER    NOT NULL
);

CREATE TABLE IF NOT EXISTS user_pok (
   id_pok    INTEGER    NOT NULL,
   id_user   INTEGER    NOT NULL
);

ALTER TABLE Ranking  ADD FOREIGN KEY (id_user)    REFERENCES Usuario(id_user);
ALTER TABLE Medalha  ADD FOREIGN KEY (id_user)    REFERENCES Usuario(id_user);
ALTER TABLE Medalha  ADD FOREIGN KEY (id_torneio) REFERENCES Torneio(id_torneio);
ALTER TABLE Torneio  ADD FOREIGN KEY (id_local)   REFERENCES Local_(id_local);
ALTER TABLE Pok_Tipo ADD FOREIGN KEY (id_pok)     REFERENCES Pokemon(id_pok);
ALTER TABLE Pok_Tipo ADD FOREIGN KEY (id_tipo)    REFERENCES Tipo(id_tipo);
ALTER TABLE user_pok ADD FOREIGN KEY (id_pok)     REFERENCES Pokemon(id_pok);
ALTER TABLE user_pok ADD FOREIGN KEY (id_user)    REFERENCES Usuario(id_user);