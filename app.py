from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'Autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'Autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'James Clear',
        'Autor': 'Hábitos Atômicos'
    },
    {
        'id': 4,
        'título': 'Rich Dad, Poor Dad',
        'Autor': 'Robert Kiyosaki'
    },
    {
        'id': 5,
        'titulo': 'Icebreaker',
        'Autor': 'Hannah Grace'
    },
]

@app.route('/books', methods=['GET'])
def consult_books():
    """
    Consults all the books.

    Returns:
        JSON: A JSON object containing all the books.
    """
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    """
    Retrieves a book by its ID.

    Args:
        id (int): The ID of the book to retrieve.

    Returns:
        JSON: A JSON object containing the book information.
    """
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

@app.route('/books/<int:id>', methods=['PUT'])
def edit_book(id):
    """
    Edits a book by its ID.

    Args:
        id (int): The ID of the book to edit.

    Returns:
        JSON: A JSON object containing the updated book information.
    """
    altered_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(altered_book)
            return jsonify(books[index])

@app.route('/books', methods=['POST'])
def new_book():
    """
    Creates a new book.

    Returns:
        JSON: A JSON object containing the updated list of books.
    """
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    """
    Deletes a book by its ID.

    Args:
        id (int): The ID of the book to delete.

    Returns:
        JSON: A JSON object containing the updated list of books.
    """
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    return jsonify(books)

app.run(port=5002, host='localhost', debug=True)
