from flask import Flask, render_template, request
app = Flask(__name__)

import pyrebase
config = {

    "apiKey": "AIzaSyDDRmqllUVPYrwiBRutWB0pBVbAxE7v9SE",
    "authDomain": "pythondev-229207.firebaseapp.com",
    "databaseURL": "https://pythondev-229207.firebaseio.com",
    "projectId": "pythondev-229207",
    "storageBucket": "",
    "messagingSenderId": "59631211876"
  # once code is pasted change it into python dictionary format into " "
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


@app.route('/')
def index():
    context = {
    'state' : 0
    }
    return render_template("index.html", **context)

@app.route('/login')
def login():
    return render_template("login.html")

# POST - Login values passed as a file from the browser to the flask server
# GET - Login values passed in the URL from the browser to the flask server

@app.route('/getting_logged', methods=['POST','GET'])
def getting_logged():
    if request.method == "POST":
        email = request.form["uemail"]
        pswd = request.form["pswd"]
        try:
            user = auth.sign_in_with_email_and_password(email,pswd)
            if user:
                return "Hi, you r logged in"
        except:
            return "Wrong credential"
    return "Something wrong"


@app.route('/data/<val>')
def data(val):
    return val



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
