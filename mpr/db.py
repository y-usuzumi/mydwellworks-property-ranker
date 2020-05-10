from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy import Column, Boolean, Integer, BigInteger, Float, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.event import listen
from geoalchemy2 import Geometry
from .env import get_mod_spatialite_name

Base = declarative_base()


class Property(Base):
    __tablename__ = 'property'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    address = Column(String)
    location = Column(Geometry(geometry_type='POINT', management=True))
    rent = Column(Float)
    parking_fee = Column(Float)
    size = Column(Float)  # squared meter
    typ = Column(String)  # apartment/condo
    included_utilities = Column(String)
    excluded_utilities = Column(String)
    archived = Column(Boolean)
    date_available = Column(Date)


def _load_spatialite(dbapi_conn, connection_record):
    dbapi_conn.enable_load_extension(True)
    mod_spatialite_name = get_mod_spatialite_name()
    dbapi_conn.load_extension(mod_spatialite_name)


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

    @contextmanager
    def session(self):
        sess = self.new_session()
        yield sess
        sess.commit()
