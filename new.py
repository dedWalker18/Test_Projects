from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    '''this is help for func hello
    '''
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
