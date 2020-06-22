import sqlalchemy
from sqla_softdelete import SoftDeleteMixin
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.types import DateTime
from datetime import datetime

db = sqlalchemy


class Base(SoftDeleteMixin):
    __soft_delete__ = True

    now = datetime.today().strftime('%Y-%m-%d')

    @declared_attr
    def created_at(cls):
        return db.Column(db.DateTime, nullable=False, default=cls.now)

    @declared_attr
    def updated_at(cls):
        return db.Column(db.DateTime, nullable=False, default=cls.now)

    @declared_attr
    def deleted_at(cls):
        return db.Column(db.DateTime) if cls.__soft_delete__ else None

    def serialize(self):
        # Transforms a model to a dictionary
        dict_repr = {
            c.name: getattr(self, c.name).isoformat()
            if isinstance(c.type, DateTime) and getattr(self, c.name) is not None
            else getattr(self, c.name)
            for c in self.__table__.columns
        }

        return dict_repr


BaseModel = declarative_base(cls=Base)
