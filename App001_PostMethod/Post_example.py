from flask import Flask,request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == "Ayush" and password == "Pranay":
        return "Welcome %s" %username

if __name__=='__main__':
    app.run(debug = True)
