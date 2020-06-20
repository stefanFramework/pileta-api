import sqlalchemy
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.types import DateTime

db = sqlalchemy

class Base():
    __soft_delete__ = True

    @declared_attr
    def created_at(cls):
        return db.Column(db.DateTime, nullable=False)

    @declared_attr
    def updated_at(cls):
        return db.Column(db.DateTime, nullable=False)

    @declared_attr
    def deleted_at(cls):
        return db.Column(db.DateTime) if cls.__soft_delete__ else None

BaseModel = declarative_base(cls=Base)
