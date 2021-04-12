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
from main import *

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
    # print(len(cat))
    cat.sort()
    # print(cat[567])
    # print(cat[2018])
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
    db.user.insert_one(req_data)
    return  {"msg":"done"}

@app.route("/calculate", methods=['POST'])
def calcu():
    req_data = request.get_json()
    print(req_data)
    username = req_data['username']
    func_type = req_data["type"]
    keywords = req_data["keywords"]
    if(req_data["time"]=='None'):
        deadline = None
    else :
        deadline = int(req_data["time"])
        
    ranked_func, ranked_info = give_ans(func_type, keywords, deadline, 5)
    # print(ranked_func)
    # print(ranked_info)
    user_publ = db.user.find_one({"username": username})[func_type]
    res = [i for i, val in enumerate(ranked_func) if val in user_publ]
    read = [0]*5
    for ind in res:
        read[ind] = 1
    
    for info in ranked_info:
        info[0]=int(info[0])
        info[1]=int(info[1])
        info[2]=int(info[2])

    # print(read)
    return {"doc_name" : ranked_func,"doc_info" : ranked_info, "doc_status" : read}
 

app.run(host='127.0.0.1', port=3000, debug=True)

#{'username': 'kriti', 'type': 'journal', 'keywords': ['accounting (q2)', 'analysis (q1)', 'genetics', 'accounting (q2)', 'analysis (q1)', 'genetics'], 'time': '9'}
# ["Annales de l'Institut Henri Poincare. Annales: Analyse Non Lineaire/Nonlinear Analysis", 'Geometric and Functional Analysis', 'Archive for Rational Mechanics and Analysis', 'Analysis and PDE', 'Calculus of Variations and Partial Differential Equations']
# [[496, 2, 6], [502, 1, 5], [526, 2, 4], [784, 1, 3], [809, 1, 3]]
