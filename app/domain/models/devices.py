from domain.models import ModelBase, db


class Device(ModelBase):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ip = db.Column(db.String, nullable=False)
    notes = db.Column(db.Text, nullable=True)
