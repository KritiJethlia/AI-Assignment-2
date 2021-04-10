from flask import Flask, render_template,url_for
from flask import request
from flask_cors import CORS
import json
from flask import jsonify
from bson import ObjectId
from flask_pymongo import pymongo
from pymongo import MongoClient

# Connecting with MongoDB database
client = pymongo.MongoClient("mongodb+srv://ai:ai@cluster0.51nej.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.user
# user_collection = pymongo.collection.Collection(db,'user_collection')

app = Flask(__name__)
CORS(app)
app.config["DEBUG"]= True

@app.route("/")
def index():
    '''
    Renders the login page.
    '''
    # user = db.user.find()
    # print(user)
    return render_template("login.html") 



app.run(host='0.0.0.0', port=3000, debug=True)