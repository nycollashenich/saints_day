from sqlalchemy import create_engine, Column, Integer, String, Enum, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum

Base = declarative_base()

class GenderEnum(enum.Enum):
    Male = 'm'
    Famele = 'f'


class Saint(Base):
    __tablename__ = 'saints'
    id = Column(Integer, primary_key=True)
    saint_day = Column(String(200), nullable=False)
    name = Column(String(100), nullable=False)
    gender = Column(Enum(GenderEnum), nullable=False)
    patron_city = Column(String(200), nullable=False)
    born = Column(Integer, nullable=False)
    died = Column(Integer, nullable=False)
    birthplace = Column(String(200), nullable=False)
    deathplace = Column(String(200), nullable=False)
    protector_of = Column(Text, nullable=True)
    image_path = Column(String(200), nullable=True)

DATABASE_URL = 'sqlite:///saint.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

print('Db created')