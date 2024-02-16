import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, JSON, func, LargeBinary
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import URL

# Load environment variables from the .env file
load_dotenv()

# Define the connection string
connection_string = URL.create(
    'postgresql',
    username=os.environ.get('NEON_USERNAME'),
    password=os.environ.get('NEON_PASSWORD'),
    host=os.environ.get('NEON_HOST'),
    database=os.environ.get('NEON_DATABASE')
)

# Create the database engine
engine = create_engine(connection_string)

Base = declarative_base()


# Define models
class User(Base):
    __tablename__ = 'Users'

    UserID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Login = Column(String, unique=True, nullable=False)
    PasswordHash = Column(String, nullable=False)
    Devices = relationship('Device', back_populates='User')


class Device(Base):
    __tablename__ = 'Devices'

    DeviceID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    Icon = Column(LargeBinary, nullable=False)
    Brand = Column(String, nullable=False)
    Model = Column(String, nullable=False)
    Type = Column(String, nullable=False)
    LastUpdate = Column(DateTime, default=func.now(), nullable=False)
    User = relationship('User', back_populates='Devices')
    Activities = relationship('Activity', back_populates='Device')


class Activity(Base):
    __tablename__ = 'Activities'

    WorkoutID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    DeviceID = Column(Integer, ForeignKey('Devices.DeviceID'))
    Data = Column(JSON, nullable=False)
    DataType = Column(String, nullable=False)
    UploadDate = Column(DateTime, default=func.now(), nullable=False)
    Device = relationship('Device', back_populates='Activities')


# Usunięcie istniejących tabel
# Base.metadata.drop_all(engine)
#
# # Tworzenie tabel
# Base.metadata.create_all(engine)
