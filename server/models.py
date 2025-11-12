# server/models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Use naming convention to avoid Alembic issues
metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'
