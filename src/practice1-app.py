# https://www.geeksforgeeks.org/python/flask-creating-first-simple-application/

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
# Primer intento, devolviendo el formato html de toda la vida
# from flask import Flask

# Segundo intento, devolviendo una salida en json
from flask import Flask, jsonify

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/api/v1/details')
# ‘/’ URL is bound with details() function.
def details():
    # html normal
    # return '<h1>Hello Julia</h1>'
    # json format
    return jsonify({
        'message': 'Hello Julia'
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({'status': 'UP'}), 200

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()


# '/api/v1/details'
# '/api/v1/healthz'