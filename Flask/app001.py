from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Olá Mundo"
@app.route('/')
def oi():
    return "oi"

app.run()
