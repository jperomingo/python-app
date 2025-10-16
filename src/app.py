# https://www.geeksforgeeks.org/python/flask-creating-first-simple-application/

from flask import Flask, jsonify
import datetime
import socket
app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        'Message': 'Hello Julia',
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname()        
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({'status': 'UP'}), 200

if __name__ == '__main__':

    app.run()