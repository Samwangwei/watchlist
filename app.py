from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/index/<name>')
def say(name):
    return '<h1>Hello ' + name + '!</h1><img src="http://helloflask.com/totoro.gif">'


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0')
