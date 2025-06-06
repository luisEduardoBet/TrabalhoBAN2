from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from ..teste import db

print(db)

class Base(DeclarativeBase):
    pass