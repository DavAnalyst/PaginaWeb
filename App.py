from flask import Flask, request, render_template, redirect
from flask_pymongo import PyMongo, ObjectId

app = Flask(__name__) # iniciar el servidor
app.config["MONGO_URI"] = 'mongodb+srv://yeisonniev:nievedinho.123@cluster0.5rqd9px.mongodb.net/DataBaseMerpes?retryWrites=true&w=majority&appName=Cluster0'
mongo = PyMongo(app)

db = mongo.db

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_user', methods = ['POST'])
def createUser():
    new_user = {
       'name': request.form['Name'],
       'email': request.form['Email'],
       'password': request.form['Password']
    }
    db.Users.insert_one(new_user)
    return redirect('/')
    
    
if __name__  == "__main__":
    app.run(debug=True)


