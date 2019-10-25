from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

# dummy data

BOOKS = [
    { 
        'id': uuid.uuid4().hex,
        'title': 'Things Fall Apart',
        'author': 'Chinua Achebe',
        'started_reading': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Aminal Farm',
        'author': 'George Orwell',
        'started_reading': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Wizard of the Crow',
        'author': 'Ngugi wa Thiong\'o',
        'started_reading': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Poor Economics',
        'author': 'Abhijit Banerjee',
        'started_reading': False
    }
    
]
#config
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# test route
@app.route('/ping',methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# All books route
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'started_reading': post_data.get('started_reading')
        })
        response_object['message'] = 'Book added!'
    else:
        respose_object['books'] = BOOKS
            
    return jsonify(response_object)

# Single book route
@app.route('/books/<book_id>', methods=['PUT'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'started_reading': post_data.get('started_reading')
        })
        response_object['message'] = 'Book updated!'
    return jsonify(response_object)

def remove_book(book_id): 
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False
if __name__== '__main__':
    app.run()