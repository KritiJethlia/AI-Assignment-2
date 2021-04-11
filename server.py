from flask import Flask, render_template,url_for
from flask import request
from flask_cors import CORS
import json
from flask import jsonify
from bson import ObjectId
from flask_pymongo import pymongo
from pymongo import MongoClient
from give_names import *
from time import time

# Connecting with MongoDB database
client = pymongo.MongoClient("mongodb+srv://ai:ai@cluster0.51nej.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.user
user_collection = pymongo.collection.Collection(db,'user')

app = Flask(__name__)
CORS(app)
app.config["DEBUG"]= True

@app.route("/")
def signin():
    '''
    Renders the login page.
    '''
    # user = db.user.find()
    # print(user)
    return render_template("login.html") 

@app.route("/find/")
def index():
    cat = give_cat()
    return render_template("index.html", categories = cat) 

@app.route("/register/")
def register():
    t1 = time()
    journals, conferences = give_names()
    print(time()-t1)
    return render_template("register.html", journals=journals, conferences=conferences) 

@app.route("/newuser", methods=['POST'])
def newreg():
    req_data = request.get_json()
    print(req_data)
    print(db.user.insert_one(req_data))
    return  {"msg":"done"}

app.run(host='127.0.0.1', port=3000, debug=True)