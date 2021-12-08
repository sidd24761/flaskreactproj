from datetime import datetime, timedelta
import hashlib, jwt, werkzeug
import logging

from flask.cli import DispatchingApp

from flask.json import jsonify
from flask import app, request, make_response,Response
from flask.templating import render_template
from models import *
from functools import wraps

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


# If you programmatically wants to create the database then use create_all() function
db.create_all()
db.session.commit()

app.config['SECRET_KEY'] = 'keyissecured12123'


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('jwt') 
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            print(token)
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
            print(data)
            current_user = data['user']

        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated

#First Flask code to display Hello World
@app.route('/test')
def hello_world():
    return "Hello World"


#Create an index page
@app.route('/')
def indexPage():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    return render_template('index.html')


#creating login page
@app.route('/login/')
def loginPage():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    return render_template('login.html')


#creating register page
@app.route('/register/')
def registerPage():
    # app.logger.info('Info level log')
    # app.logger.warning('Warning level log')
    return render_template('register.html')

@app.route('/registersuccess', methods=["POST"])
def registerSuccess():
    # app.logger.info('Info level log')
    # app.logger.warning('Warning level log')
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        #hashing the password before storing
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()

        entry = Users(name=name,email=email,password=hashedPassword)
        db.session.add(entry)
        db.session.commit()
    return render_template('login.html')

@app.route('/loginsuccess', methods=['POST'])
def loginSucess():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #hashing the input and comparing the hash
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        result = db.session.query(Users).filter(Users.email==email, Users.password==hashedPassword)
        for row in result:
            if (len(row.email)!=0):
                print(row.email)
                token = jwt.encode({'user':row.email, 'exp': datetime.utcnow()+timedelta(minutes=15)}, app.config['SECRET_KEY'])
                print("Token ",token)
                return make_response(jsonify({'jwt' : token}), 201)
    return make_response('could not verify', 401, {'WWW-Authenticate':'Basic="Login Required"'})


@app.route('/dashboard')
@token_required
def dashboard(current_user): # http://127.0.0.1:8000/dashboard?jwt=
    return render_template('dashboard.html', data=current_user)

@app.errorhandler(werkzeug.exceptions.BadRequest)
def badRequest(e):
    # app.logger.info('Info level log')
    # app.logger.warning('Warning level log')
    return "Bad request", 400
app.register_error_handler(400, badRequest)

@app.errorhandler(404)
def notFound(e):
    return "Page not found", 404
app.register_error_handler(404,notFound )

#Check for the docs of error https://flask.palletsprojects.com/en/2.0.x/errorhandling/
#HTTP Codes https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

if __name__ == "__main__":
    app.run(debug=True, port=8000)

#logging -> reference https://www.askpython.com/python-modules/flask/flask-logging
# Five levels of debugging
# debug, info, warning, error, critical
