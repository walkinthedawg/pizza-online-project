import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'online-pizza'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    the_user = mongo.db.users.find({'username': username})
    return render_template("login.html", the_user = the_user)
                          
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")
    
@app.route('/create', methods=['GET', 'POST'])
def create():
    users =  mongo.db.users
    users.insert_one(request.form.to_dict())
    firstname = request.form.get('firstname')
    return render_template("create.html", firstname = firstname)    
    
@app.route('/toppings')
def toppings():
    return render_template("toppings.html", 
                           toppings=mongo.db.toppings.find())
    
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    return render_template("checkout.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)