from flask import Flask, render_template, request, jsonify ,  redirect, url_for
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo.server_api import ServerApi
import json

app = Flask(__name__)
# FLASK
cluster = MongoClient("mongodb+srv://boab:1234@cluster0.d3aixga.mongodb.net/?retryWrites=true&w=majority")
db = cluster["user_database"]
collection = db["user"]

cursor = collection.find({})

for document in cursor:
    print(document)

@app.route('/')
def index():
    
    return render_template('logreg.html')

@app.route('/korzi' , methods=['GET'])
def korzi():
    return render_template('korzi.html')

@app.route('/carta',  methods=['GET'])
def carta():
    return render_template('carta.html')

@app.route('/index' , methods=['GET'])
def register():
    return render_template('index.html')


@app.route('/logreg', methods=['POST'])
def logreg():
    
    data = request.get_json()
    print(data)
    # data2 = json.loads(data)
    # print(data2)
    username = data['signup-email']
    
    
    
    if collection.find_one({'signup-email': username}):
        return jsonify({'error': 'Имя пользователя уже занято!'})
    else:
        print("Abob")
        collection.insert_one(data)
        
    return redirect(url_for('index'))
    
    


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['signup-email']
    password = data['signup-password']

    user = collection.find_one({'username': username})

    if user and check_password_hash(user['signup-password'], password):
        return jsonify({'message': 'Авторизация успешна!'})
    else:
        return jsonify({'error': 'Неверное имя пользователя или пароль!'})
    


@app.route('/index', methods=['POST'])
def visaCard():
    dannyi = request.get_json()
    cardNumber = dannyi['CardNumber']
    CARDHOLDER = dannyi['CardHolder']
    EXPIRATIONMM= dannyi['Date']
    YY = dannyi['years']
    Cvv = dannyi['CVV']
    if (collection.find_one({'CardNumber' : cardNumber})):
        return -1
    else :
        collection.insert_many(dannyi)


if __name__ == '__main__':
    app.run(debug=True , port = 8080)
