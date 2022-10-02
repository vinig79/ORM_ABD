from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey

# <dbms>[+<driver>]://<user>:<pass>@<host>[:<port>][/<database>]
URL='mysql+mysqlconnector://vinig79:vinig79@127.0.0.1:3306/ABD_ORM'
engine = create_engine(url=URL)

Base = declarative_base()

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

class Tipo(Base):
    __tablename__ = "Tipo"
    id_tipo = Column(Integer, primary_key=True)
    tipo = Column(String(150), nullable=False)

class Usuario(Base):
    __tablename__ = "Usuario"
    id_user = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)

class Rankin(Base):
    __tablename__ = "Ranking"
    id_user = Column(Integer, ForeignKey("Usuario.id_user"), primary_key=True)
    position = Column(Integer, nullable=False)
    vitorias = Column(Integer, nullable=False)

class Local_(Base):
    __tablename__ = "Local_"
    id_local = Column(Integer, primary_key=True)
    local_ = Column(String(150), nullable=False)

class Torneio(Base):
    __tablename__ = "Torneio"
    id_torneio = Column(Integer, primary_key=True)
    id_local = Column(Integer, ForeignKey("Local_.id_local"), nullable=False)
    nome = Column(String(150), nullable=False)

class Medalha(Base):
    __tablename__ = "Medalha"
    medal_id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("Usuario.id_user"))
    nome = Column(String(150), nullable=False)
    id_torneio = Column(Integer, ForeignKey("Torneio.id_torneio"))

class Pok_tipo(Base):
    __tablename__ = "Pok_tipo"
    id_pok = Column(Integer,ForeignKey("Pokemon.id_pok"), primary_key=True)
    id_tipo = Column(Integer,ForeignKey("Tipo.id_tipo"), primary_key=True)

class user_pok(Base):
    __tablename__ = "user_pok"
    id_pok = Column(Integer, ForeignKey("Pokemon.id_pok"), primary_key=True)
    id_user = Column(Integer, ForeignKey("Usuario.id_user"), primary_key=True)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

