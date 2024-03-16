from flask import Flask, jsonify, request
from flask_cors import CORS
import os



app = Flask(__name__)
cors = CORS(app)

@app.route('/book_image/<ean>', methods=['GET'])
def get_images(ean):
    if os.path.isfile('static/images/'+ ean + '.jpg'):
        return jsonify({
            'ean' : ean,
            'url' : "http://51.75.21.24:3252/static/images/" + ean + '.jpg'
        }), 200
    else:
        return jsonify({
            'error' : 'This book has no cover yet',
            'url' : "http://51.75.21.24:3252/static/images/no_cover.jpg"
        }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3252)
