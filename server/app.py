from flask import Flask
from models import db, Pet
import os

app = Flask(__name__, instance_relative_config=True)

db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pets.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Ensure the instance folder exists if using Option A
os.makedirs(app.instance_path, exist_ok=True)

db.init_app(app)

# Create tables and seed data
with app.app_context():
    db.create_all()
    if not Pet.query.first():
        db.session.add_all([
            Pet(name="Fido", species="Dog"),
            Pet(name="Whiskers", species="Cat"),
            Pet(name="Tweety", species="Bird"),
        ])
        db.session.commit()

@app.route("/pets")
def get_pets():
    pets = Pet.query.all()
    return {"pets": [{"id": p.id, "name": p.name, "species": p.species} for p in pets]}


if __name__ == "__main__":
    app.run(debug=True)
