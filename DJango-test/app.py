# import collections
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# from flask import Flask, render_template
# from flask import Flask, render_template, request, jsonify
# from pymongo import MongoClient

# app = Flask(__name__)
# # FLASK
# uri = "mongodb+srv://boab:1234@cluster0.d3aixga.mongodb.net/?retryWrites=true&w=majority"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# db = client.user_database
# coll = db.user


# # Send a ping to confirm a successful connection

# client.admin.command('ping')
# print("Pinged your deployment. You successfully connected to MongoDB!")

# @app.route('/')
# def index():
#     return render_template('registration.html')

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()

#     # Сохранение данных в MongoDB
#     coll.insert_one(data)

#     return jsonify({'message': 'Регистрация успешна!'})

# if __name__ == '__main__':
#     app.run(debug=True , port=8080)

# from flask import Flask, render_template, request, jsonify
# from pymongo import MongoClient
# from werkzeug.security import generate_password_hash, check_password_hash
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# from flask import Flask, render_template
# from flask import Flask, render_template, request, jsonify
# from pymongo import MongoClient

# app = Flask(__name__)
# # FLASK
# uri = "mongodb+srv://boab:1234@cluster0.d3aixga.mongodb.net/?retryWrites=true&w=majority"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))


# db = client.user_database
# coll = db.user


# @app.route('/')
# def index():
#     return render_template('registration.html')

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     username = data['username']

#     # Проверка уникальности имени пользователя
#     if coll.find_one({'username': username}):
#         return jsonify({'error': 'Имя пользователя уже занято!'})


#     # Хэширование пароля
#     hashed_password = generate_password_hash(data['password'], method='sha256')
#     data['password'] = hashed_password

#     # Сохранение данных в MongoDB
#     coll.insert_one(data)

#     return jsonify({'message': 'Регистрация успешна!'})

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data['username']
#     password = data['password']

#     user = coll.find_one({'username': username})

#     if user and check_password_hash(user['password'], password):
#         return jsonify({'message': 'Авторизация успешна!'})
#     else:
#         return jsonify({'error': 'Неверное имя пользователя или пароль!'})

# if __name__ == '__main__':
#     app.run(debug=True , port = 8080)

from flask import Flask, render_template, request, jsonify ,  redirect, url_for
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo.server_api import ServerApi
import json

app = Flask(__name__)
# FLASK
uri = "mongodb+srv://boab:1234@cluster0.d3aixga.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))



db = client.user_database
coll = db.user

@app.route('/')
def index():
    
    return render_template('logreg.html')

@app.route('/index')
def chat():
    return render_template('index.html')

@app.route('/logreg', methods=['POST'])
def logreg():
    
    data = request.get_json()
    # data2 = json.loads(data)
    # print(data2)
    username = data['signup-email']
    
    
    
    if coll.find_one({'signup-email': username}):
        return jsonify({'error': 'Имя пользователя уже занято!'})
    else:
        print("Abob")
        coll.insert_one(data)
        
    return redirect(url_for('index'))
    


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['signup-email']
    password = data['signup-password']

    user = coll.find_one({'username': username})

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
    if (coll.find_one({'CardNumber' : cardNumber})):
        return -1
    else :
        coll.insert_many(dannyi)


if __name__ == '__main__':
    app.run(debug=True , port = 8080)
