from flask import Flask, jsonify, request

app = Flask(__name__)

# An example data source (dictionary)
books = [
    {
        'id': 1,
        'title': 'Python ile Programlama',
        'author': 'John Doe'
    },
    {
        'id': 2,
        'title': 'Flask ile Web Geliştirme',
        'author': 'Jane Smith'
    }
]

# Endpoint to list all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Single book fetch endpoint
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Add new book endpoint
@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.json
    if 'title' not in new_book or 'author' not in new_book:
        return jsonify({'message': 'Missing Value'}), 400

    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

# book deletion endpoint
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
