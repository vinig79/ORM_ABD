from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table

# <dbms>[+<driver>]://<user>:<pass>@<host>[:<port>][/<database>]
URL="mysql+mysqlconnector://aluno:aluno123@localhost/Pokedex"
engine = create_engine(url=URL)

Base = declarative_base()

Pok_tipo =Table('Pok_tipo', Base.metadata, Column("id_pok", Integer, ForeignKey("Pokemon.id_pok")),Column('id_tipo', Integer, ForeignKey('Tipo.id_tipo')))
user_pok = Table('user_pok', Base.metadata, Column("id_user", Integer, ForeignKey('Usuario.id_user')), Column('id_pok', Integer, ForeignKey('Pokemon.id_pok')))


class Pokemon(Base):
    __tablename__ = "Pokemon"
    id_pok = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    hp = Column(Integer, nullable=False)
    atk = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    atk_special = Column(Integer, nullable=False)
    special_defense = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)
    tipo = relationship("Tipo", secondary=Pok_tipo)

class Tipo(Base):
    __tablename__ = "Tipo"
    id_tipo = Column(Integer, primary_key=True)
    tipo = Column(String(150), nullable=False)

class Usuario(Base):
    __tablename__ = "Usuario"
    id_user = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    raking = relationship('Ranking', uselist=False, back_populates='usuario')

class Rankin(Base):
    __tablename__ = "Ranking"
    id_user = Column(Integer, ForeignKey("Usuario.id_user"), primary_key=True)
    position = Column(Integer, nullable=False)
    vitorias = Column(Integer, nullable=False)
    usuario = relationship("Usuario",back_populates="ranking")

class Local_(Base):
    __tablename__ = "Local_"
    id_local = Column(Integer, primary_key=True)
    local_ = Column(String(150), nullable=False)

class Torneio(Base):
    __tablename__ = "Torneio"
    id_torneio = Column(Integer, primary_key=True)
    id_local = Column(Integer, ForeignKey("Local_.id_local"), nullable=False)
    nome = Column(String(150), nullable=False)
    medalha = relationship('Medalha')


class Medalha(Base):
    __tablename__ = "Medalha"
    medal_id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("Usuario.id_user"))
    nome = Column(String(150), nullable=False)
    id_torneio = Column(Integer, ForeignKey("Torneio.id_torneio"))

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

