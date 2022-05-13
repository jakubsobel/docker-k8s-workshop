from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

bookList = [
    {
        'id': 1,
        'title': 'The Face of the Lost',
    },
    {
        'id': 2,
        'title': 'Rain of Broken Things',
    },
    {
        'id': 3,
        'title': 'The Sealed Time',
    },
]

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/books')
def books(): 
  return jsonify(bookList)

app.run(host='0.0.0.0', port=80, debug=True)
