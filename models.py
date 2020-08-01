"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
 
class Cupcake(db.Model):
    """cupcake."""

    def __repr__(self):
        """Show info about cupcake."""

        c = self
        return f"<Pet {p.id} {p.name} {p.species} {p.hunger}>"

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.Text,
                     nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image=db.Column(db.Text, default="https://tinyurl.com/demo-cupcake")

    def serialize(self):
        """return a serialized version of the data"""
        return{
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }