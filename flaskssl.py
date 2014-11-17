from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':

    #app.run('0.0.0.0', debug=True, port=8443, ssl_context=('host.crt', 'host.key'))
    app.run('0.0.0.0', debug=True, port=8443,
         ssl_context='adhoc')
