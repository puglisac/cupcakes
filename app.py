"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from models import db, connect_db, Cupcake
from forms import CupcakeForm
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "some_secret_key"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)


@app.route("/")
def home_page():
    """displays a home page"""
    form = CupcakeForm()
    return render_template("home.html", form=form)


@app.route("/api/cupcakes")
def all_cupcakes():
    """returns all cupcakes in the db"""
    data = request.args['data']
    cupcakes = Cupcake.query.filter(Cupcake.flavor.ilike(f"%{data}%"))
    cake_list = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes=cake_list)


@app.route("/api/cupcakes/<int:id>")
def cupcake_details(id):
    """returns details about a specific cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def add_cupcake():
    """creates a new cupcake"""
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)


@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def edit_cupcake(id):
    """edits an existing cupcake"""
    data = request.json
    cupcake = Cupcake.query.get_or_404(id)
    db.session.query(Cupcake).filter_by(id=id).update(data)
    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    """deletes an existing cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")
