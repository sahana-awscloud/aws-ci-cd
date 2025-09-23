from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to python flask app hosted on AWS EC2 instance'

if __name__ == '__main__':
    app.run()
