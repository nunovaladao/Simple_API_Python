# Book Management API 🛠️📚

## Introduction
- The Book Management API is a Flask-based web application that provides endpoints for managing a collection of books. It allows users to perform operations such as retrieving all books, retrieving a specific book by its ID, creating a new book, updating an existing book, and deleting a book. 
- I made this project just for fun to learn about API's.

## Installation

1. Make sure you have Python 3 installed on your system.
2. Clone this repository to your local machine:
``` bash
git clone https://github.com/nunovaladao/Simple_API_Python.git
```
3. Navigate to the project directory:
``` bash
cd Simple_API_Python
```
4. Install the required dependencies using pip - pip3 if you're in a mac:
``` bash
pip3 install flask
pip3 install requests
``` 

## Usage

1. Run the Flask application:
``` bash
python app.py
``` 
2. Interact with the API using a tool like **Postman** or a **web browser**. Below are the available endpoints:
- `GET /books: Retrieve all books`
- `GET /books/<id>: Retrieve a book by its ID.`
- `PUT /books/<id>: Update a book by its ID.`
- `POST /books: Create a new book`
- `DELETE /books/<id>: Delete a book by its ID.`
**Note:** Replace <id> with the actual ID of the book.

##
Nuno Valadão | nsoares-@student.42porto.com