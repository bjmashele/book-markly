from flask import Flask, jsonify, request
from flask_cors import CORS

# dummy data

BOOKS = [
    {
        'title': 'Things Fall Apart',
        'author': 'Chinua Achebe',
        'started_reading': True
    },
    {
        'title': 'Aminal Farm',
        'author': 'George Orwell',
        'started_reading': True
    },
    {
        'title': 'Wizard of the Crow',
        'author': 'Ngugi wa Thiong\'o',
        'started_reading': True
    },
    {
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

# get all books
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        respose_object['books'] = BOOKS
            
    return jsonify(response_object)

if __name__== '__main__':
    app.run()