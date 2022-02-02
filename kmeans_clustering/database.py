import pypyodbc as podbc
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

con = podbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=H510I\SQLEXPRESS;"
    "Database=customers;"
    "Trusted_Connection=yes;"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=con)

Base = declarative_base()
