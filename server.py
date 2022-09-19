from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hola():
    return 'hola mundo'

@app.route('/dojo')
def dojo():
    return 'hola mundo, dojo'

@app.route('/dojo/<string:name>')
def say(name):
    return 'hola mundo ' + name

@app.route('/dojo/<int:rep>/<string:name>')
def home(rep, name):
    return render_template('index.html', rep = rep, name = name)

@app.errorhandler(404)
def access_error(error):
    return render_template('errores.html'), 404

if __name__=="__main__":
    app.run(debug = True)





