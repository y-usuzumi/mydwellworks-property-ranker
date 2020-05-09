from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.event import listen
from geoalchemy2 import Geometry

Base = declarative_base()


class Property(Base):
    __tablename__ = 'property'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    address = Column(String)
    location = Column(Geometry(geometry_type='POLYGON', management=True))


def _load_spatialite(dbapi_conn, connection_record):
    dbapi_conn.enable_load_extension(True)
    dbapi_conn.load_extension('mod_spatialite')


class DB:
    def __init__(self, conn_str, echo=True):
        engine = create_engine(conn_str, echo=echo)
        listen(engine, 'connect', _load_spatialite)
        conn = engine.connect()
        conn.execute(select([func.InitSpatialMetaData(1)]))
        conn.close()
        Base.metadata.bind = engine
        Base.metadata.create_all()
        self._engine = engine
        self._sessionmaker = sessionmaker(bind=engine)

    def new_session(self):
        return self._sessionmaker()
