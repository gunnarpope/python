from flask import Flask
app = Flask(__name__)

@app.route('/user/<name>')
def hello(name):
    return 'Hello %s!' % name

if __name__ == '__main__':
    # Listen any client host
    # Never use debug mode in product project
    app.run(host='0.0.0.0', debug=True)
